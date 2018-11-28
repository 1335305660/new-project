from flask import Flask, Session
from flask_sqlalchemy import SQLAlchemy
from redis import StrictRedis
from flask_wtf import CSRFProtect
from flask_session import Session
from config import config_dict



def create_app(config_name):
    # 模块文件夹　用户模块profile : new: 登陆注册模块：admin
    app = Flask(__name__)
    config_class = config_dict["config_name"]
    app.config.from_object(config_class)

    db = SQLAlchemy(app)

    redis_store = StrictRedis(host=config_class.REDIS_HOST, port=config_class.REDIS_PORT)
    # 给项目添加防护机制
    CSRFProtect(app)

    Session(app)

    return app

