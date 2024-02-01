from extends import db
from datetime import datetime


# 商品分类表，3级分类
class CategoryGoods(db.Model):
    __tablename__ = 'category_goods'
    id = db.Column(db.Integer, primary_key=True, nullable=False)  # 分类id
    name = db.Column(db.String(40), nullable=False)  # 分类名
    goods_num = db.Column(db.Integer, default=0)  # 商品数量
    is_show = db.Column(db.Boolean, default=1)  # 是否显示
    is_menu = db.Column(db.Boolean, default=1)  # 是否导航
    seq = db.Column(db.Integer, nullable=True)  # 排序
    parent_id = db.Column(db.Integer, index=True)  # 上级分类id
    template_id = db.Column(db.Integer)  # 模板id
    # channel = db.relationship('GoodsChannel', back_populates='Category')


# 商品频道表，对应所有一级分类，一一对应
# class GoodsChannel(db.Model):
#     __tablename__ = 'goods_channel'
#     id = db.Column(db.Integer, primary_key=True, nullable=False)  # 频道id
#     # group_id = db.Column(db.Integer,  db.ForeignKey('channel_group'))  # 所属商品组
#     category_id = db.Column(db.Integer, db.ForeignKey('goods_category.id'))  # 商品类别
#     sequence = db.Column(db.Integer)  # 组内排序序号
#     Category = db.relationship('GoodsCategory', back_populates='channel')
#     channelGroup = db.relationship('ChannelGroup', back_populates='channel')

# 首页商品频道组，对应商品频道表， 一一对应，这里功能我没使用
# class ChannelGroup(db.Model):
#     __tablename__ = 'channel_group'
#     id = db.Column(db.Integer, primary_key=True, nullable=False)  # 频道组id
#     name = db.Column(db.String(40), nullable=False)  # 频道组名
#     url = db.Column(db.varchar(100))
#     channel = db.relationship('GoodsChannel', backref='channelGroup')


# 商品品牌表
class Brand(db.Model):
    __tablename__ = 'brand'
    id = db.Column(db.BigInteger, primary_key=True, nullable=False)  # 商品品牌id
    name = db.Column(db.String(100), nullable=False)  # 商品品牌名
    image = db.Column(db.String(100))  # 品牌图片地址
    letter = db.Column(db.String(3))  # 品牌首字母
    seq = db.Column(db.Integer, nullable=True)  # 排序
    # spu = db.relationship('Spu', back_populates='brand')


# 品牌分类表
class CategoryBrand(db.Model):
    category_id = db.Column(db.Integer, primary_key=True, nullable=False)  # 分类id
    brand_id = db.Column(db.Integer, primary_key=True, nullable=False)  # 品牌id


# 商品标准单元spu
class Spu(db.Model):
    __tablename__ = 'spu'
    id = db.Column(db.BigInteger, primary_key=True, nullable=False)  # 商品表id
    sn = db.Column(db.String(60))  # 货号
    name = db.Column(db.String(100))  # SPU名
    caption = db.Column(db.String(100))  # 副标题
    brand_id = db.Column(db.Integer)  # 品牌id
    category1_id = db.Column(db.Integer)  # 一级类别id
    category2_id = db.Column(db.Integer)  # 二级类别id
    category3_id = db.Column(db.Integer)  # 三级类别id
    template_id = db.Column(db.Integer)  # 模板id
    freight_id = db.Column(db.Integer)  # 运费模板id
    image = db.Column(db.String(100))  # 图片
    images = db.Column(db.String(1000))  # 图片列表
    sale_service = db.Column(db.String(50))  # 售后服务
    introduction = db.Column(db.Text)  # 介绍
    spec_items = db.Column(db.String(3000))  # 规格列表
    para_items = db.Column(db.String(3000))  # 参数列表
    sale_num = db.Column(db.Integer, default=0)  # 销量
    comment_num = db.Column(db.Integer, default=0)  # 评论数
    is_marketable = db.Column(db.SmallInteger, default=0)  # 是否上架，0已下架，1已上架
    is_enable_spec = db.Column(db.SmallInteger, default=1)  # 是否启用规格，0否，1是
    is_delete = db.Column(db.SmallInteger, default=0)  # 是否删除， 0未删除， 1已删除
    status = db.Column(db.SmallInteger, default=1)  # 审核状态， 0未审核，1已审核，2审核不通过
    # brand = db.relationship('Brand', back_populates='spu')
    # sku = db.relationship('Sku', back_populates='spu')


# 商品库存表sku
class Sku(db.Model):
    __tablename__ = 'sku'
    id = db.Column(db.BigInteger, primary_key=True, nullable=False)  # 商品id
    sn = db.Column(db.String(100), nullable=False)  # 商品条码
    name = db.Column(db.String(40))  # sku名称
    price = db.Column(db.BigInteger, nullable=False)  # 价格(分)
    num = db.Column(db.Integer, nullable=False)  # 库存数量
    alert_num = db.Column(db.Integer)  # 库存预警数量
    image = db.Column(db.String(200))  # 商品图片
    images = db.Column(db.String(2000))  # 商品图片组
    weight = db.Column(db.Integer)  # 重量(克)
    create_time = db.Column(db.Time, default=datetime.now)  # 创建的日期时间
    update_time = db.Column(db.Time, default=datetime.now, index=True)  # 更新时的日期时间
    spu_id = db.Column(db.BigInteger)  # 商品spu_id
    category_id = db.Column(db.Integer, index=True)  # 商品分类id
    category_name = db.Column(db.String(200))  # 商品分类名称
    brand_name = db.Column(db.String(100))  # 商品品牌名称
    spec = db.Column(db.String(200))  # 商品规格
    sale_num = db.Column(db.Integer)  # 销量
    comment_num = db.Column(db.Integer)  # 评论数
    status = db.Column(db.SmallInteger, index=True)  # 商品状态 1-正常，2-下架，3-删除
    # spu = db.relationship('Spu', back_populates='sku')


# 参数表
class Para(db.Model):
    __tablename__ = 'para'
    id = db.Column(db.Integer, primary_key=True, nullable=False,
                   autoincrement=True)  # 参数id
    name = db.Column(db.String(50))  # 参数名
    options = db.Column(db.String(2000))  # 选项
    seq = db.Column(db.Integer, nullable=True)  # 排序
    template_id = db.Column(db.Integer)  # 模板id
    # spu = db.relationship('Spu', back_populates='specification')


# 商品规格选项表
class Spec(db.Model):
    __tablename__ = 'spec'
    id = db.Column(db.Integer, primary_key=True, nullable=False,
                   autoincrement=True)  # 参数id
    name = db.Column(db.String(50))  # 参数名
    options = db.Column(db.String(2000))  # 规格选项
    seq = db.Column(db.Integer, nullable=True)  # 排序
    template_id = db.Column(db.Integer)  # 模板id
    # spu = db.relationship('Spu', back_populates='specification')


# 活动表
class Pref(db.Model):
    __tablename__ = 'pref'
    id = db.Column(db.Integer, primary_key=True, nullable=False,
                   autoincrement=True)  # 参数id
    category_id = db.Column(db.Integer)  # 分类id
    buy_money = db.Column(db.Integer)  # 消费金额
    pre_money = db.Column(db.Integer)  # 优惠金额
    start_time = db.Column(db.Time)  # 活动开始时间
    end_time = db.Column(db.Time)  # 活动结束时间
    type = db.Column(db.SmallInteger)  # 1-普通订单， 2-限时活动
    state = db.Column(db.SmallInteger)  # 状态 1-有效，0-无效


# 模板表
class Template(db.Model):
    __tablename__ = 'template'
    id = db.Column(db.Integer, primary_key=True, nullable=False,
                   autoincrement=True)  # 模板id
    name = db.Column(db.String(50))  # 模板名
    spec_num = db.Column(db.SmallInteger, default=0)  # 规格数量
    para_num = db.Column(db.SmallInteger, default=0)  # 参数数量
