from flask import Blueprint, request, session
from utils import generate_token, verify_token
from flask import make_response
from .captcha_tool import GenerateCaptcha
from .user_db_model import Captcha, SmsCaptcha, User
from nanoid import generate
from extends import db
import re
# 创建蓝图
user_bp = Blueprint('user', __name__, url_prefix='/', static_folder='./static')


# 发图形验证码接口
@user_bp.route('/captcha/image')
def captcha():
    # 取验证码
    img_byt, code = GenerateCaptcha().draw_verify_image()
    # 验证码图片标识21个字符
    key = generate()
    print(key, code)
    # 存入数据库
    captcha_my = Captcha(key=key, code=code)
    db.session.add(captcha_my)
    db.session.commit()
    # 发送至前端
    # img_byt byt转str，否则json无法格式化
    data = {
        "status": 200,
        "message": "success",
        "data": {
            'base64': img_byt.decode("utf-8"),
            'key': key
        }
    }
    return data


# 发短信验证码接口
@user_bp.route('/captcha/sendSmsCaptcha', methods=('POST', ))
def send_sms_captcha():
    data = request.get_json()
    print('@', data['captchaCode'], data['captchaKey'], data['mobile'])
    # 校验手机号码
    if data.get('mobile'):
        ret = re.match(r"^1[3-9][0-9]{9}$", data.get('mobile'))
        if not ret:
            return {"status": 300, "message": '手机号格式错误', "data": []}
        else:
            phone = User.query.filter(User.phone == data['mobile']).first()
            if not phone:
                # 这里去保存用户手机号到数据库
                user = User(phone=data['mobile'])
                db.session.add(user)
                db.session.commit()
    else:
        return {"status": 300, "message": '请求参数"mobile"缺失或为空', "data": []}
    # 校验验证码是否传递
    if not data.get('captchaCode'):
        return {"status": 300, "message": '请求参数"captchaCode"缺失或为空', "data": []}
    # 校验验证码key,对应的验证码是否准确
    if data.get('captchaKey'):
        code = Captcha.query.filter_by(key=data.get('captchaKey')).first()
        if code and data.get('captchaCode').lower() == code.code.lower():
            # 删除数据库的图形验证码
            # db.session.delete(code)
            # db.session.commit()
            # 发送云服务短信验证码功能模块写这里调用，生成手机验证码6位，保存
            sms_captcha = 123456
            sms = SmsCaptcha(phone=data.get('mobile'), captcha=sms_captcha)
            db.session.add(sms)
            db.session.commit()
            status = 200
            message = '发送成功，请注意查收'
        else:
            status = 300
            message = '验证码校验错误'
    else:
        status = 300
        message = '请求参数"captchaCode"缺失或为空'
    return {
        "status": status,
        "message": message,
        "data": []
    }


# 手机验证码登录接口
@user_bp.route('/passport/login', methods=('POST',))
def login():
    data = request.get_json()
    # print(data['isParty'], data['partyData'], data['mobile'], data['smsCode'])
    if data.get('isParty'):
        # 第三方登录逻辑
        pass
    if data.get('mobile') and data.get('smsCode'):
        ret = re.match(r"^1[3-9][0-9]{9}$", data.get('mobile'))
        if not ret:
            return {"status": 300, "message": '手机号格式错误', "data": {}}
        else:
            sms_captcha1 = SmsCaptcha.query.filter_by(phone=data.get('mobile')).first()
            if sms_captcha1 and sms_captcha1.captcha != data.get('smsCode'):
                return {"status": 300, "message": '手机验证码错误', "data": {}}
    else:
        return {"status": 300, "message": '传递的必需参数缺失或为空', "data": {}}
    # 生成token发前端
    user = User.query.filter_by(phone=data.get('mobile')).first()
    userid = user.id
    my_token = generate_token(userid=userid, username=data.get('mobile'))
    # print(my_token)
    # 删除数据库手机验证码一条记录
    sms_captcha1 = SmsCaptcha.query.filter_by(phone=data.get('mobile')).first()
    db.session.delete(sms_captcha1)
    db.session.commit()
    data_send = {
        "status": 200,
        "message": "登录成功",
        "data": {
            "userId": userid,
            "token": my_token
        }
    }
    return data_send


if __name__ == '__main__':
    pass
