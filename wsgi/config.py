class BaseConfig:
    JSON_AS_ASCII = False
    DEBUG = False


class DevConfig(BaseConfig):
    DEBUG = True
