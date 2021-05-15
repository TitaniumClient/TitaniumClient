import psutil
from pypresence import Presence
import time

client_id = '843193480683192320'  # Fake ID, put your real one here
RPC = Presence(client_id,pipe=0)  # Initialize the client class
RPC.connect() # Start the handshake loop


while True:  # The presence will stay on as long as the program is running
    cpu_per = round(psutil.cpu_percent(),1) # Get CPU Usage
    mem = psutil.virtual_memory()
    mem_per = round(psutil.virtual_memory().percent,1)
    RPC.update(details="Playing Titanium Client")
    time.sleep(15) # Can only update rich presence every 15 seconds