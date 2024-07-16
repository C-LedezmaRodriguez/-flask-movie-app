import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'supersecretkey'
    TMDB_API_KEY = os.environ.get('TMDB_API_KEY') or 'your_tmdb_api_key'

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

config = {
    'development': DevelopmentConfig,
    'default': DevelopmentConfig
}
