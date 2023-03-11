from util.env_config_base import EnvConfigBase


class Config(EnvConfigBase):
    _CONFIG_SUFFIX = 'EMB_'
    SQLITE_FILE = 'data/balance.db'
    ALERT_NUMBER: int = 20
    TO_MAIL = ''
    ROOM_ID = ''
    USER_ID = ''
    SMTP_HOST = ''
    SMTP_PORT: int = ''
    SMTP_USER = ''
    SMTP_PASSWORD = ''
    GET_BALANCE_JSON_DATA_ID = ''
    GET_BALANCE_JSON_DATA_DEVICE_CODE = ''
    GET_BALANCE_JSON_DATA_DEVICE_ID = ''
    GET_BALANCE_JSON_DATA_PRODUCT_ID = ''


config = Config()
