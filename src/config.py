"""Module contains all flask config classes"""
import os
from typing import Optional


class BaseConfig:
    SECRET_KEY: Optional[str] = os.environ.get("SECRET_KEY")
    TESTING: bool = False
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False
    FLASK_DEBUG: int = 1


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI: Optional[str] = os.environ.get("DATABASE_URL")


class TestingConfig(BaseConfig):
    TESTING: bool = True
    SQLALCHEMY_DATABASE_URI: Optional[str] = os.environ.get(
        "DATABASE_TEST_URL"
    )


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI: Optional[str] = os.environ.get("DATABASE_URL")
    DEBUG = False
