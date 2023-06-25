# File: flash_rpc.py
# Project: flash-discord-RPC
# File Created: Saturday, ‎June ‎24, ‎2023, ‏‎10:26:38 AM
# Author: Dooji (doojisbasement@gmail.com)
# GitHub: https://github.com/dooji2
# Discord: dooji_

# Last Modified: ‎Saturday, ‎June ‎24, ‎2023, ‏‎8:28:34 PM
# Modified By: Dooji (doojisbasement@gmail.com)

# Copyright (c) 2023 Dooji
import time
import os
from pypresence import Presence
import psutil

# Initialize the RPC client with your application's client ID
client_id = "1122093746402627604"
RPC = Presence(client_id)
RPC.connect()

for process in psutil.process_iter():
        if "flash" in process.name(): 
            # Flash process found, get the full command line
            flash_command = " ".join(process.cmdline())
            if "swf" in flash_command:
                game_name = flash_command.split(os.path.sep)[-1]
        else: 
            RPC.clear()
            





def recheck(game_name):
    for process in psutil.process_iter():
        if "flash" in process.name(): 
            # Flash process found, get the full command line
            flash_command = " ".join(process.cmdline())
            if "swf" in flash_command:
                game_name = flash_command.split(os.path.sep)[-1]
                if game_name == "papaspizzeria_v2.swf":
                    
                    
                    RPC.update(details="Playing Papa's Pizzeria", large_image="pizza", small_image="flash")
                    
                elif game_name == "papaswingeria.swf":
                    
                    RPC.update(details="Playing Papa's Wingeria", large_image="wing", small_image="flash")
                elif game_name == "papasbakeria.swf":
                    
                    RPC.update(details="Playing Papa's Bakeria", large_image="bake", small_image="flash")
                elif game_name == "papasburgeria.swf":
                    
                    RPC.update(details="Playing Papa's Burgeria", large_image="burger", small_image="flash")
                elif game_name == "papascheeseria_102.swf":
                    
                    RPC.update(details="Playing Papa's Cheeseria", large_image="cheese", small_image="flash")
                elif game_name == "papascupcakeria.swf":
                    
                    RPC.update(details="Playing Papa's Cupcakeria", large_image="cupcake", small_image="flash")
                elif game_name == "papasdonuteria.swf":
                    
                    RPC.update(details="Playing Papa's Donuteria", large_image="donut", small_image="flash")
                elif game_name == "papasfreezeria.swf":
                    
                    RPC.update(details="Playing Papa's Freezeria", large_image="freezeria", small_image="flash")
                elif game_name == "papashotdoggeria.swf":
                    
                    RPC.update(details="Playing Papa's Hot Doggeria", large_image="hotdog", small_image="flash")
                elif game_name == "papaspancakeria.swf":
                    
                    RPC.update(details="Playing Papa's Pancakeria", large_image="pancake", small_image="flash")
                elif game_name == "papaspastaria.swf":
                    
                    RPC.update(details="Playing Papa's Pastaria", large_image="pasta", small_image="flash")
                elif game_name == "papasscooperia_v102.swf":
                    
                    RPC.update(details="Playing Papa's Scooperia", large_image="scoop", small_image="flash")
                elif game_name == "papassushiria.swf":
                    
                    RPC.update(details="Playing Papa's Sushiria", large_image="sushi", small_image="flash")
                elif game_name == "papastacomia.swf":
                    
                    RPC.update(details="Playing Papa's Taco Mia!", large_image="taco", small_image="flash")
        
                
            
                    

# Update the Rich Presence data
#RPC.update(
#    small_image="flash"
#)

# Keep the script running
while True:
    if "flash" not in process.name(): RPC.clear()
    recheck(game_name)
    time.sleep(5)  # Update the presence every 15 seconds
    
# Disconnect the RPC client when done
RPC.close()

