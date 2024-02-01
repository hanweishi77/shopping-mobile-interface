from extends import db
from datetime import datetime


# 首页展示区图片集
class ContentCategory(db.Model):
    __tablename__ = 'content_category'
    id = db.Column(db.Integer, primary_key=True, nullable=False)  # 广告类别id
    name = db.Column(db.String(30))  # 广告类别名
    tag = db.Column(db.String(30))  # 类别识别键名
    created_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间


class Content(db.Model):
    __tablename__ = 'content'
    id = db.Column(db.Integer, primary_key=True, nullable=False)  # 广告id
    category_id = db.Column(db.Integer, db.ForeignKey('content_category.id'))  # 商品类别
    title = db.Column(db.String(40))  # 广告标题
    url = db.Column(db.String(100))  # 内容页面地址
    image = db.Column(db.String(100))  # 广告图片地址
    text = db.Column(db.String(200))  # 广告文本内容
    sequence = db.Column(db.SmallInteger)  # 同类广告排序
    status = db.Column(db.Boolean)  # 是否展示
    created_time = db.Column(db.DateTime, index=True, default=datetime.now)  # 创建时间
