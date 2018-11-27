from flask import Flask, Session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf import CSRFProtect
from flask_session import Session
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from config import Config


# class Config(object):
#     #DEBUG = True
#     SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/python22"
#     SQLALCHEMY_TRACK_MODIFICATIONS = False
#     SECRET_KEY = "ASJFJKSA1465879"
#     # redis数据库配置信息
#     REDIS_HOST = "127.0.0.1"
#     REDIS_PORT = 6379
#
#     # 将session 存储的数据从内存转移到ｒｅｄｉｓ中存储的配置信息中去
#     SESSION_TYPE = "redis"
#     SESSION_REDIS = StrictRedis(REDIS_HOST, REDIS_PORT)
#     SESSION_USE_SIGNER = True
#     # 设置数据不需要永久保存，　而是根据我们设置的过期时长进行调整
#     SESSION_PERMANENT = False
#
#     PERMANENT_SESSION_LIFETIME = 86400 # 24小时


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

redis_store = StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)
# 给项目添加防护机制
CSRFProtect(app)

Session(app)
# 创建管理类
manger = Manager(app)
# 7. 创建数据库迁移对象
Migrate(app, db)

# 8 添加迁移命令
manger.add_command("db", MigrateCommand)


@app.route('/')
def index():
    return 'hello world!'


if __name__ == '__main__':
    # print(app.url_map)
    # app.run(debug=True)
    manger.run()
