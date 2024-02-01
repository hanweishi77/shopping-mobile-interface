class Config:
    # 通讯密钥，WTF表单post提交需要,session也需要
    SECRET_KEY = "fadfadfafdsffadfadf"
    # 开启debug
    DEBUG = True
    # 连接mysql数据库的配置
    HOSTNAME = "127.0.0.1"  # 本机
    PORT = 3306  # 端口
    USERNAME = "root"  # 连接用户
    PASSWORD = "123456"  # 用户密码
    DATABASE = "shopping_mobile_db"  # 数据库
    DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
    # SQLALCHEMY_DATABASE_URI为系统变量名
    SQLALCHEMY_DATABASE_URI = DB_URI
    # 设置是否跟踪数据库的修改情况，一般不跟踪
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # 数据库操作时后台是否显示原始SQL语句
    SQLALCHEMY_ECHO = False
