import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    TMDB_API_KEY = os.environ.get('TMDB_API_KEY')

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
