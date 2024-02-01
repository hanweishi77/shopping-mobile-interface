from flask import Blueprint, request, session
from utils import generate_token, verify_token
from flask import make_response
from .advert_db_model import ContentCategory, Content
# from .db_model import TbGoodsChannel, TbChannelGroup, TbBrand, TbSpu
# from .db_model import TbSku, TbSpuSpecification, TbSpecificationOption, TbSkuImage, TbSkuSpecification
from nanoid import generate
from extends import db
import re
# 创建蓝图
advert_bp = Blueprint('advert', __name__, url_prefix='/', static_folder='./static', static_url_path='/advertisement/static')

