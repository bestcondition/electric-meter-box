import config


def get_balance():
    import requests

    json_data = dict(config.GET_BALANCE_JSON_DATA)

    response = requests.post(
        'https://dsuser.zjzxdq.com/aep/ctwingdevice/manualQueryBalance',
        json=json_data,
    )

    balance = response.json()['data']
    return float(balance)
