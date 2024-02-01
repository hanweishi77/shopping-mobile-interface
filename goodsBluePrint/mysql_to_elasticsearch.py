from .goods_db_model import Spu
from elasticsearch import Elasticsearch


# 创建商品索引库
def mappings():
    return {
        "mappings": {
          "properties": {
              "goods_id": {
                  "type": "keyword",  # keyword不会分词
                  "index": "false"  # 默认创建倒排索引，false-不创建
              },
              "goods_name": {
                  "type": "text",  # text会分词
                  "analyzer": "ik_smart",  # 最大粗粒度分词
              },
              "goods_caption": {
                  "type": "text",
                  "analyzer": "ik_smart",
              },
              "brand_id": {
                  "type": "keyword",
                  "index": "false"
              },
              "category1_id": {
                  "type": "keyword",
                  "index": "false"
              },
              "category2_id": {
                  "type": "keyword",
                  "index": "false"
              },
              "category3_id": {
                  "type": "keyword",
                  "index": "false"
              },
              "image": {
                  "type": "keyword",
                  "index": "false"
              },
              "images": {
                  "type": "keyword",
                  "index": "false"
              },
              "sale_servie": {
                  "type": "keyword",
                  "index": "false"
              },
              "introduction": {
                  "type": "text",
                  "analyzer": "ik_smart"
              },
              "spec_items": {
                  "type": "keyword",
                  "index": "false"
              },
              "para_items": {
                  "type": "keyword",
                  "index": "false",
              },
              "sale_num": {
                  "type": "integer",
                  "index": "false"
              },
              "comment_num": {
                  "type": "integer",
                  "index": "false"
              },
              "is_marketable": {
                  "type": "short",
                  "index": "false"
              },
              "is_enable_spec": {
                  "type": "short",
                  "index": "false"
              },
              "is_delete": {
                  "type": "short",
                  "index": "false"
              },
              "status": {
                  "type": "short",
                  "index": "false"
              }
          }
        }
    }


# 把取出的数据写入到elasticsearch
def write_elasticsearch(es, index="index_goods"):
    # 创建ES索引-如存在则不创建
    list_es_index = [line.split() for line in es.cat.indices().splitlines()][0]
    print('@', index, list_es_index, index in list_es_index)
    if index not in list_es_index:
        es.indices.create(index=index, body=mappings())
    # 从mysql数据库获取商品spu库所有数据
    spu = Spu.query.all()

    def get_spu_db(row):
        # 准备数据
        return {
            "goods_id": row["sn"],
            "goods_name": row["name"],
            "goods_caption": row["caption"],
            "brand_id": row["brand_id"],
            "category1_id": row["category1_id"],
            "category2_id": row["category2_id"],
            "category3_id ": row["category3_id "],
            "image": row["image"],
            "images": row["images"],
            "sale_servie": row["sale_servie"],
            "introduction": row["introduction"],
            "spec_items": row["spec_items"],
            "para_items": row["para_items"],
            "sale_num": row["sale_num"],
            "comment_num": row["comment_num"],
            "is_marketable": row["is_marketable"],
            "is_enable_spec": row["is_enable_spec"],
            "is_delete": row["is_delete"],
            "status": row["status"]
        }
    try:
        for row_spu in spu:
            print(row_spu['status'])
            # res = es.index(index=index, body=get_spu_db(row_spu), id=row_spu['sn'])
            # print(res)
    except Exception as e:
        print('ES编制索引错误：', e)
