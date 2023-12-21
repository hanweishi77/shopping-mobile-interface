
import jwt
from datetime import datetime, timedelta
from config import Config
from functools import wraps


# 生成token
def generate_token(userid, username, duration=3600):
    """
    :param userid:
    :param username:
    :param duration: ‘默认3600秒’
    :return: token
    """
    exp = datetime.utcnow() + timedelta(seconds=duration)
    # header为可选，默认即为以下内容，如需修改加密算法、token类型，可以设置该内容
    header = {
        'alg': 'HS256',
        'typ': 'jwt'
    }
    # payload 加密体，  Reserved claims推荐使用有>>> 'exp'：过期时间戳，'iss','sub','sud','iat'
    # public claims 根据需要定义自己的字段.  private claims 自定义字段
    payload = {
        'userid': userid,
        'username': username,
        'exp': exp
    }
    # 签名需要key，headers，payload
    token = jwt.encode(payload=payload, key=Config.SECRET_KEY, headers=header)
    return token


# 验证token
def verify_token(token):
    """
    :param token: jwt加密str
    :return: dict对象
    """
    key = Config.SECRET_KEY
    payload_ = None
    msg = None
    status = 100
    try:
        payload_ = jwt.decode(jwt=token, key=key, algorithms="HS256")
    except jwt.exceptions.DecodeError:
        msg = '认证失败'
        status = 500
    except jwt.exceptions.ExpiredSignatureError:
        msg = '签名过期'
        status = 300
    except jwt.exceptions.InvalidAlgorithmError:
        msg = '无效算法错误'
        status = 400

    if payload_:
        return {'payload_': payload_, 'msg': '认证成功', 'status': 200}
    else:
        return {'msg': msg, 'status': status}


# 验证是否登录
def verify_login(fn):
    """
    登录验证装饰器
    """
    @wraps(fn)
    def inner_fn(*args, **kwargs):
        if 'token':
            pass
        return fn(*args, **kwargs)
    return inner_fn

