class Config:
    SECRET_KEY = '3bhotel'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Limit168@rm-bp1n49bnpp75h7jcpko.mysql.rds.aliyuncs.com:3306/pmall'

    @staticmethod
    def init_app(app):
        pass

config = {
    'development': DevelopmentConfig,

    'default': DevelopmentConfig
}
