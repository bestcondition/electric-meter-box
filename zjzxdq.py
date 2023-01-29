import config


def get_balance():
    import requests

    params = {
        'roomId': config.ROOM_ID,
        'userId': config.USER_ID,
    }

    response = requests.get('https://dsuser.zjzxdq.com/room/roomdevice/getDefultDevice', params=params)
    return response.json()['data']['balance']
