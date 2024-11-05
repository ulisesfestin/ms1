from asyncio.log import logger
from dotenv import load_dotenv
from pathlib import Path
import os

basedir = os.path.abspath(Path(__file__).parents[2])
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    TESTING = False
    
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    TESTING = True
    DEBUG = True
    CONNECTION_STRING = os.getenv('CONNECTION_STRING')
    OTEL_SERVICE_NAME = os.getenv('OTEL_SERVICE_NAME')
        
class ProductionConfig(Config):
    DEBUG = False
    TESTING = False
    
    @classmethod
    def init_app(cls, app):
        Config.init_app(app)

def factory(app):
    configuration = {
        'development': DevelopmentConfig,
        'production': ProductionConfig
    }
    
    return configuration[app];