import time
import weather_parcer
import psutil
from pypresence import Presence


def discord_rich_presence():

    image = 'saber'
    image_text = 'saber'
    client_id = '1154071316425613312'  # Fake ID, put your real one here
    RPC = Presence(client_id, pipe=0)  # Initialize the client class
    RPC.connect()  # Start the handshake loop

    while True:
        # Replace 'desired_region' with the region you want weather data for
        desired_region = "Yakutsk"  # Replace with your desired region
        weather_data = weather_parcer.get_weather(desired_region)

        # Access the weather values
        temp_now = weather_data['temp_now']
        dayhour = weather_data['dayhour']
        emoji = weather_data['emoji']

        cpu_per = round(psutil.cpu_percent(), 1)  # Get CPU Usage
        psutil.virtual_memory()
        mem_per = round(psutil.virtual_memory().percent, 1)
        print(RPC.update(
            large_image=f"{image}",
            large_text=f"{image_text}",
            details="RAM: " + str(mem_per) + "%" "   CPU: " + str(cpu_per) + "%",
            state=f"{temp_now}°{emoji}  {dayhour}",
            buttons = [
                {'label': 'LYS', 'url': 'https://www.youtube.com/watch?v=KWrFdEhyKjg'}
            ]
        ))

        time.sleep(15)  # Can only update rich presence every 15 seconds


if __name__ == '__main__':
    discord_rich_presence()

