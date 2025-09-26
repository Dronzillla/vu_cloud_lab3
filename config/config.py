class Config:
    SECRET_KEY = "VerySecretKey"
    SQLALCHEMY_DATABASE_URI = "sqlite:///./app.db"


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///./test.db"
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SERVER_NAME = "127.0.0.1:5000"
