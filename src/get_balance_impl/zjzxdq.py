from config import config


def get_balance():
    import requests

    json_data = {
        'id': config.GET_BALANCE_JSON_DATA_ID,
        'deviceCode': config.GET_BALANCE_JSON_DATA_DEVICE_CODE,
        'deviceId': config.GET_BALANCE_JSON_DATA_DEVICE_ID,
        'productId': config.GET_BALANCE_JSON_DATA_PRODUCT_ID,
    }

    response = requests.post(
        'https://dsuser.zjzxdq.com/aep/ctwingdevice/manualQueryBalance',
        json=json_data,
    )

    balance = response.json()['data']
    return float(balance)
