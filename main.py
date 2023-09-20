from pypresence import Presence
import time
import requests
import weather

image = 'saber'
image_text = 'saber'
state = 'Tasks done...'
party_size = [1, 2]
    
def discord_status():
    start = int(time.time())
    client_id = "1154071316425613312"
    RPC = Presence(client_id)
    RPC.connect()
    

    while True:
        RPC.update(
            large_image=f'{image}',
            large_text=f'{image_text}',
            state=f'{state}',
            details=f'{weather.emoji} {weather.time}',
            party_size=party_size,
            start=start,
            buttons=[
                {'label': 'KYS', 'url': 'https://www.google.com'},
                {'label': 'Discord', 'url': 'https://discord.com'}
            ]
        )
        time.sleep(60)


if __name__ == '__main__':
    discord_status()
    weather.emoji_formatting()
