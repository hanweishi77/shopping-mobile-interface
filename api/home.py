
from flask import Blueprint, request
from advertBluePrint.advert import get_banner, get_newsflash, get_big_picture, get_channel

# 创建蓝图
api_bp = Blueprint('api', __name__, url_prefix='/', static_folder='./static', static_url_path='/api/static')


# 首页数据接口
@api_bp.route('/page/detail', methods=('GET', ))
def get_index():
    data = request.get_json()
    page = data.get("page") | 1

    return {
        "status": 200,
        "message": "success",
        "data": {
            "pageData": {
                "page": {
                    "name": "页面设置",
                    "type": "page",
                    "params": {
                        "name": "hh",
                        "title": "智慧商城",
                        "shareTitle": "分享标题"
                    },
                    "style": {
                        "titleTextColor": "white",
                        "titleBackgroundColor": "#c21401"
                    }
                },
                "items": [
                    {
                        "name": "banner",
                        "type": "search",
                        "data": []
                    },
                    {

                    }
                ]
            }
        }
    }
