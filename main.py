from pypresence import Presence
import time
import requests
import weather


def discord_status():
    start = int(time.time())
    client_id = "1154071316425613312"
    RPC = Presence(client_id)
    RPC.connect()
    dsize = 10000000000000000000000000000000000000000000000000000000000
    while True:
        RPC.update(
            large_image='saber',
            large_text='saber',
            state=f'Dick size - {dsize}',
            details=f'Temp: {weather.temp}',
            party_size=[1, 2],
            start=start,
            buttons=[
                {'label': 'KYS', 'url': 'https://www.google.com'},
                {'label': 'Discord', 'url': 'https://discord.com'}  # Added a valid URL
            ]
        )
        time.sleep(60)


if __name__ == '__main__':
    discord_status()
