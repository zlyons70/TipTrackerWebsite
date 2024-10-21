import redis

class ApplicationConfig:
    '''This class is used to store the configuration for the application'''
    SESSION_TYPE = 'redis'
    SESSION_PERMANENT = False
    SESSION_USE_SIGNER = True
    SESSION_REDIS = redis.Redis(host='localhost', port=6379)
    SESSION_KEY_PREFIX = 'flask_session'