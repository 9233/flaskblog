# -*- coding: utf-8 -*-
import os
import sys
import hashlib
from flask import current_app, render_template
from flask.app import Flask

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))


# SQLite URI compatible
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'


class BaseConfig(object):
    SECRET_KEY = os.getenv('SECRET_KEY') or hashlib.new(name='md5', string='FLASKBLOG python@#').hexdigest()

    DEBUG_TB_INTERCEPT_REDIRECTS = False

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_ECHO = False

    MAIL_SERVER = os.getenv('MAIL_SERVER')
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = ('FLASKBLOG Admin', MAIL_USERNAME)

    FLASKBLOG_TITLE = os.getenv('FLASKBLOG_TITLE','flaskBlog')
    FLASKBLOG_DOMAIN = os.getenv('FLASKBLOG_DOMAIN','www.flaskBlog.com')
    FLASKBLOG_KEYWORDS = os.getenv('FLASKBLOG_KEYWORDS','python,flask,个人博客')
    FLASKBLOG_DESCRIPTION = os.getenv('FLASKBLOG_DESCRIPTION','flaskBlog')
    FLASKBLOG_EMAIL = os.getenv('FLASKBLOG_EMAIL','')
    FLASKBLOG_POST_PER_PAGE = 10
    FLASKBLOG_MANAGE_POST_PER_PAGE = 15
    FLASKBLOG_COMMENT_PER_PAGE = 15
    FLASKBLOG_SLOW_QUERY_THRESHOLD = 1
    FLASKBLOG_REGISTER_INVITECODE = os.getenv('FLASKBLOG_REGISTER_INVITECODE',False)   # 是否开启邀请码注册
    FLASKBLOG_COMMENT = os.getenv("FLASKBLOG_COMMENT", False) # 是否开发评论，默认不开启
    FLASKBLOG_EDITOR = os.getenv('FLASKBLOG_EDITOR', 'markdown') # 默认编辑器
    FLASKBLOG_TEMPLATE = os.getenv('FLASKBLOG_TEMPLATE', 'tend') # 前端模板

    FLASKBLOG_UPLOAD_TYPE = os.getenv('FLASKBLOG_UPLOAD_TYPE','') # 默认本地上传
    FLASKBLOG_UPLOAD_PATH = os.path.join(basedir, 'uploads')
    FLASKBLOG_ALLOWED_IMAGE_EXTENSIONS = ['png', 'jpg', 'jpeg', 'gif', 'webp']
    FLASKBLOG_TONGJI_SCRIPT = os.getenv('FLASKBLOG_TONGJI_SCRIPT','') #统计代码
    FLASKBLOG_EXTEND_META = os.getenv('FLASKBLOG_EXTEND_META', '') # 扩展META
    FLASKBLOG_ROBOTS = os.getenv('FLASKBLOG_ROBOTS', 'User-agent: *\nAllow: /') # 网站robots定义

    MAX_CONTENT_LENGTH = 32 * 1024 * 1024

    QINIU_CDN_URL = os.getenv('QINIU_CDN_URL','http://cdn.FLASKBLOG.com/')
    QINIU_BUCKET_NAME = os.getenv('QINIU_BUCKET_NAME','FLASKBLOG')
    QINIU_ACCESS_KEY = os.getenv('QINIU_ACCESS_KEY','key123')
    QINIU_SECRET_KEY = os.getenv('QINIU_SECRET_KEY','secret456')

    BAIDU_PUSH_TOKEN = os.getenv('BAIDU_PUSH_TOKEN') #主动推送给百度链接，token是在搜索资源平台申请的推送用的准入密钥

    SITEMAP_URL_SCHEME = os.getenv('SITEMAP_URL_SCHEME','http')
    SITEMAP_MAX_URL_COUNT = os.getenv('SITEMAP_MAX_URL_COUNT',100000)

    ALIPAY_APPID= os.getenv('ALIPAY_APPID', '') # 设置签约的appid
    ALIPAY_PUBLIC_KEY = os.getenv('ALIPAY_PUBLIC_KEY', '') # 支付宝公钥
    ALIPAY_PRIVATE_KEY =os.getenv('ALIPAY_PRIVATE_KEY', '') # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥
    ALIPAY_DEBUG = os.getenv('ALIPAY_DEBUG', True)
    ALIPAY_NOTIFY_URL = os.getenv('ALIPAY_NOTIFY_URL', '')
    

    

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    # 设置连接数据库的URL
    user = 'root'
    password = 'Aa123456'
    database = 'flaskblog'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'mysql+pymysql://%s:%s@localhost:3306/%s' % (user,password,database)
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data-dev.db'))

class TestingConfig(BaseConfig):
    DEBUG = True
    # 设置连接数据库的URL
    user = 'root'
    password = 'Aa123456'
    database = 'flaskblog'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'mysql+pymysql://%s:%s@localhost:3306/%s' % (
    user, password, database)
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data-dev.db'))


class ProductionConfig(BaseConfig):
    DEBUG = True
    # 设置连接数据库的URL
    user = 'root'
    password = 'Aa123456'
    database = 'flaskblog'

    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'mysql+pymysql://%s:%s@localhost:3306/%s' % (
    user, password, database)
    # SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', prefix + os.path.join(basedir, 'data-dev.db'))


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
"""
config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig
}
"""
def exist_config() -> bool:
    return _exist_config(current_app)


def _exist_config(app: Flask) -> bool:
    filename = "{}/config.py".format(app.root_path)
    return os.path.exists(filename)


def create_config(db_uri:str) -> None:
    config_name = current_app.config['CONFIG_NAME']
    import_config = 'ProductionConfig'
    if config_name == 'development':
        import_config = 'DevelopmentConfig'
    elif config_name == 'testing':
        import_config = 'TestingConfig'
    data = render_template("config.tpl", db_uri = db_uri, import_config = import_config)
    filename = '{}/config.py'.format(current_app.root_path)
    with open(filename, 'w') as f:
        f.write(data)

if __name__ == "__main__":
    pass