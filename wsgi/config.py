class BaseConfig:
    """
    Base config
    """
    JSON_AS_ASCII = False
    DEBUG = False


class DevConfig(BaseConfig):
    """
    Config for dev server
    """
    DEBUG = True
