class Config:
    SECRET_KEY = '3bhotel'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Limit168@localhost/pmall'

    @staticmethod
    def init_app(app):
        pass

config = {
    'development': DevelopmentConfig,

    'default': DevelopmentConfig
}
