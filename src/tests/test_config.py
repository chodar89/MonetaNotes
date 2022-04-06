import os


def test_development_config(test_app):
    test_app.config.from_object("src.config.DevelopmentConfig")
    assert test_app.debug is True
    assert test_app.config["TESTING"] is False
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get(
        "DATABASE_URL"
    )


def test_testing_config(test_app):
    test_app.config.from_object("src.config.TestingConfig")
    assert test_app.debug is True
    assert test_app.config["TESTING"] is True
    assert not test_app.config["PRESERVE_CONTEXT_ON_EXCEPTION"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get(
        "DATABASE_TEST_URL"
    )


def test_production_config(test_app):
    test_app.config.from_object("src.config.ProductionConfig")
    assert test_app.debug is False
    assert test_app.config["TESTING"] is False
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get(
        "DATABASE_URL"
    )
