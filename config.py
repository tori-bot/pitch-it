import os
class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://elvis:moraaelvis@localhost/pitch'

    UPLOADED_PHOTOS_DEST ='app/static/photos'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://elvis:moraaelvis@localhost/pitch'

    DEBUG=True

# class TestConfig(Config):
#     SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://elvis:moraaelvis@localhost/pitch_test'

config_options={
    'development':DevConfig,
    'production':ProdConfig,
    # 'test':TestConfig
}