from flask_sqlalchemy import SQLAlchemy
from elasticsearch import Elasticsearch

db = SQLAlchemy()
es = Elasticsearch(['http://192.168.43.85:9200'])
