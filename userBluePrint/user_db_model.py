from extends import db
from datetime import datetime


# 图形验证码存储表
class Captcha(db.Model):
    __tablename__ = 'captcha'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号，自增
    key = db.Column(db.String(25), nullable=False)  # 键值
    code = db.Column(db.String(6), nullable=False)  # 字符
    created_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
    tag = db.Column(db.Boolean, default=False)  # 状态标识

    def __repr__(self):
        return '<Captcha %r>' % self.__tablename__


# 短信验证码存储
class SmsCaptcha(db.Model):
    __tablename__ = "sms_captcha"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号，主键自增
    phone = db.Column(db.String(11), nullable=False)  # 邮箱,非空
    captcha = db.Column(db.String(6), nullable=False)  # 验证码,非空
    tag = db.Column(db.Boolean, default=False)  # 标识
    created_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间


# 会员表
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # 编号，自增
    username = db.Column(db.String(40), nullable=True)  # 用户名
    email = db.Column(db.String(40), nullable=True, unique=True)  # 邮箱
    pwd = db.Column(db.String(250), nullable=True)  # 密码
    phone = db.Column(db.String(11), unique=True)  # 手机号
    role = db.Column(db.Integer, default=0)  # 权限
    created_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 注册时间
    # user_address = db.relationship('Address', backref='user')  # 用户收藏地址外键关系关联
    # user_cart = db.relationship("Cart", backref="user")  # 用户购物车外键关系关联

    def __repr__(self):
        return '<User %r>' % self.__tablename__

    def check_pwd(self, pwd):
        """
        检测密码是否正确
        :param pwd: 密码
        :return: 返回布尔值
        """
        from werkzeug.security import check_password_hash
        return check_password_hash(self.pwd, pwd)
