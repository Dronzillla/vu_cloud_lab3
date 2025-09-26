import os


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "VerySecretKey")
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # disable warning globally


class DevelopmentConfig(Config):
    DEBUG = True
    # Development DB from env variable
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL", "postgresql://postgres:example@localhost:5432/todos_db"
    )


class ProductionConfig(Config):
    DEBUG = False
    # Production DB will be provided via DATABASE_URL env variable
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")


class TestingConfig(Config):
    TESTING = True
    # Separate database for testing
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "TEST_DATABASE_URL",
        "postgresql://postgres:example@localhost:5432/todos_test_db",
    )
    WTF_CSRF_ENABLED = False
    SERVER_NAME = "127.0.0.1:5000"
