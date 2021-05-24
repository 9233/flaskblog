from app.settings import ProductionConfig as Cfg

class Config(Cfg):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Aa123456@localhost/flaskblog?charset=utf8'