from flask import Blueprint
from .advert_db_model import Content


# 创建蓝图
advert_bp = Blueprint('advert', __name__, url_prefix='/', static_folder='./static',
                      static_url_path='/advertisement/static')


def get_banner():
    banner_content = Content.query.filter(Content.category_id == 1 and Content.status == 1)  # .order_by(Content.sequence)
    return banner_content


def get_newsflash():
    newsflash_content = Content.query.filter(Content.category_id == 2 and Content.status == 1)
    return newsflash_content


def get_big_picture():
    big_picture_content = Content.query.filter(Content.category_id == 3 and Content.status == 1)
    return big_picture_content


def get_channel():
    channel_content = Content.query.filter(Content.category_id == 4 and Content.status == 1)
    return channel_content
