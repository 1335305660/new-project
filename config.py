from redis import StrictRedis


class Config(object):
    """项目配置基类"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = "mysql://root:mysql@127.0.0.1:3306/python22"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "ASJFJKSA1465879"
    # redis数据库配置信息
    REDIS_HOST = "127.0.0.1"
    REDIS_PORT = 6379

    # 将session 存储的数据从内存转移到ｒｅｄｉｓ中存储的配置信息中去
    SESSION_TYPE = "redis"
    SESSION_REDIS = StrictRedis(REDIS_HOST, REDIS_PORT)
    SESSION_USE_SIGNER = True
    # 设置数据不需要永久保存，　而是根据我们设置的过期时长进行调整
    SESSION_PERMANENT = False

    PERMANENT_SESSION_LIFETIME = 86400 # 24小时


class DevelopmentConfig(Config):
    """开发模式的项目配置信息"""
    DEBUG = True


class ProductionConfig(Config):
    """线上模式的项目配置信息"""
    DEBUG = True


# 提供一个接口给外键使用
config_dict = {
    "development": DevelopmentConfig,
    "production": ProductionConfig
}