import os
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

    SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URI')

    UPLOADED_PHOTOS_DEST ='app/static/photos'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL").replace("://", "ql://", 1)
    DEBUG=True

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://elvis:moraaelvis@localhost/pitch'

    

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://elvis:moraaelvis@localhost/pitch_test'

config_options={
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}