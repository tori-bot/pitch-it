class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://elvis:moraaelvis@localhost/pitch'
    

class ProdConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://elvis:moraaelvis@localhost/pitch'

    DEBUG=True

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://elvis:moraaelvis@localhost/pitch_test'

config_options={
    'development':DevConfig,
    'production':ProdConfig,
    'test':TestConfig
}