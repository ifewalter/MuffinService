import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    DEVELOPMENT_DB = 'mysql://root:ifewalter@localhost/muffin'
    TESTING_DB = 'mysql://root:ifewalter@localhost/muffin_test'


class ProductionConfig(Config):
    SECURITY_PASSWORD_HASH = 'pbkdf2_sha512'
    SECURITY_TRACKABLE = True
    SECURITY_PASSWORD_SALT = 'something_super_secret_change_in_production'
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'MUFFIN_PRODUCTION_DATABASE_URI'
    )

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = Config.DEVELOPMENT_DB


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = Config.TESTING_DB


config = {
    'production': ProductionConfig,
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'default': ProductionConfig,
}
