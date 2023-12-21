from flask import Blueprint, request
from utils import generate_token, verify_token


# 创建蓝图
user_bp = Blueprint('user', __name__, url_prefix='/', static_folder='./static')


@user_bp.route('/passport/login', methods=('POST',))
def login():
    if request.method == 'POST':
        print('我收到了')
        print(request.headers.get('Access-Token'))
        print(request.headers.get('platform'))
        print(request.json)
        my_token = generate_token(userid=100003, username='14442544252')
        print(my_token)
        print(verify_token(my_token))
        return {
            "status": 200,
            "message": "登录成功",
            "data": {
                "userId": 10003,
                "token": my_token
            }
        }
