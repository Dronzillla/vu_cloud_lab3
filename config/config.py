import os
from dotenv import load_dotenv

load_dotenv()


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
    # Default option for retrieving DB URI
    # SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")
    # SQLALCHEMY_ENGINE_OPTIONS = {"connect_args": {"sslmode": "require"}}

    # Another setup for retrieving DB URI, which requires sslmode communication
    db_url = os.getenv("DATABASE_URL")

    if db_url:
        # Fix postgres:// to postgresql:// for SQLAlchemy compatibility
        if db_url.startswith("postgres://"):
            db_url = db_url.replace("postgres://", "postgresql://", 1)

        # Add sslmode=require if not already present
        if "sslmode=" not in db_url:
            if "?" in db_url:
                db_url += "&sslmode=require"
            else:
                db_url += "?sslmode=require"

    SQLALCHEMY_DATABASE_URI = db_url


class TestingConfig(Config):
    TESTING = True
    # Separate database for testing
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "TEST_DATABASE_URL",
        "postgresql://postgres:example@localhost:5432/todos_test_db",
    )
    WTF_CSRF_ENABLED = False
    SERVER_NAME = "127.0.0.1:5000"
