from flask import Flask, request
from flask import jsonify, render_template, redirect
from flask import request, jsonify
from flask_cors import CORS  # 跨域请求处理
import config
from extends import db
from userBluePrint.login import user_bp


app = Flask(__name__)
app.config.from_object(config.Config)  # 实例app的配置加载

# 要允许跨源发出Cookie或经过身份验证的请求，只需将`supports_credentials`选项设置为True即可
CORS(app, supports_credentials=True)  # 挂载到实例app，解决跨域问题

# 数据库操作对象db初始化，以及一些控制设置
db.init_app(app)

# 注册蓝图
app.register_blueprint(user_bp)


if __name__ == '__main__':
    app.run()