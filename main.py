import time
import reader
import weather_parser
import psutil
from pypresence import Presence
import time_getter


def discord_rich_presence():
    # Replace 'desired_region' with the region you want weather data for
    desired_region = "Tokyo"  # Replace with your desired region
    weather_data = weather_parcer.get_weather(desired_region)
    # Access the weather values
    client_id = '1154071316425613312'  # Fake ID, put your real one here
    RPC = Presence(client_id, pipe=0)  # Initialize the client class
    RPC.connect()  # Start the handshake loop

    while True:
        cpu_per = round(psutil.cpu_percent(), 1)  # Get CPU Usage
        psutil.virtual_memory()
        mem_per = round(psutil.virtual_memory().percent, 1)
        print(RPC.update(
            large_image=f"{reader.name}",
            large_text=f"asd",
            details="RAM: " + str(mem_per) + "%" "   CPU: " + str(cpu_per) + "%",
            state=f"{weather_data['temp_now']}°{weather_data['emoji']}  {time_getter.get_current_time()}",
            buttons=[
                {"label": reader.button1_label, "url": reader.button1_url},
                {"label": reader.button1_label, "url": reader.button2_url}
            ]
        ))

        time.sleep(15)  # Can only update rich presence every 15 seconds


if __name__ == '__main__':
    discord_rich_presence()
