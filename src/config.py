"""Module contains all flask config classes"""
import os
from typing import Optional


class BaseConfig:
    TESTING: bool = False
    SQLALCHEMY_TRACK_MODIFICATIONS: bool = False


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI: Optional[str] = os.environ.get("DATABASE_URL")


class TestingConfig(BaseConfig):
    TESTING = True
    SQLALCHEMY_DATABASE_URI: Optional[str] = os.environ.get(
        "DATABASE_TEST_URL"
    )


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI: Optional[str] = os.environ.get("DATABASE_URL")
