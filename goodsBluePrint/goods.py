from flask import Blueprint, request
from elasticsearch import Elasticsearch
from .mysql_to_elasticsearch import write_elasticsearch
from .goods_db_model import CategoryGoods, Brand, CategoryBrand, Spu, Sku, Para, Spec, Pref, Template

# 创建蓝图
goods_bp = Blueprint('goods', __name__, url_prefix='/', static_folder='./static', static_url_path='/goods/static')


# 商品搜索接口
@goods_bp.route('/goods/list', methods=('GET', ))
def search():
    # data = request.get_json()
    # 按商品搜索，商品id查找就不写了,商品分页也不写了
    # query = data.get("goodsName")
    # page = data.get("page") | 1
    es = Elasticsearch(['http://192.168.43.85:9200'])
    write_elasticsearch(es)
    # dsl = {
    #     "query": {
    #         "multi_match": {
    #             "query": '华为',
    #             "fields": ["goods_name", "goods_caption"]
    #         }
    #     }
    # }
    # results = es.search(index="shopping_mobile_db", body=dsl)
    # goods_list = []
    # for row in results.get("hits").get("hits"):
    #     goods_list.append(row.get("_source"))
    # print(goods_list)
    # data = {
    #     "status": 200,
    #     "message": "success",
    #     "data": {
    #         "list": {
    #             "total": len(goods_list),
    #             "per_page": 15,
    #             "current_page": 1,
    #             "last_page": 1,
    #             "data": goods_list
    #         }
    #     }
    # }
    return "hh"


"""
@goods_bp.route("/category/list", methods=('GET', ))
def category_list():
    pass
"""