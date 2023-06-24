# File: flash_rpc.py
# Project: flash-discord-RPC
# File Created: Saturday, ‎June ‎24, ‎2023, ‏‎10:26:38 AM
# Author: Dooji (doojisbasement@gmail.com)
# GitHub: https://github.com/dooji2
# Discord: dooji_

# Last Modified: ‎Saturday, ‎June ‎24, ‎2023, ‏‎8:37:01 PM
# Modified By: Dooji (doojisbasement@gmail.com)

# Copyright (c) 2023 Dooji
import time
import os
from pypresence import Presence
import psutil

for process in psutil.process_iter():
    if "flash" in process.name(): 
        # Flash process found, get the full command line
        flash_command = " ".join(process.cmdline())
        if "swf" in flash_command:
            game_name = flash_command.split(os.path.sep)[-1]
            if game_name == "papaspizzeria_v2.swf":
                game_name = "Papa's Pizzeria"
                lg = "pizza"
            if game_name == "papaswingeria.swf":
                game_name = "Papa's Wingeria"
                lg = "wing"
            if game_name == "papasbakeria.swf":
                game_name = "Papa's Bakeria"
                lg = "bake"
            if game_name == "papasburgeria.swf":
                game_name = "Papa's Burgeria"
                lg = "burger"
            if game_name == "papascheeseria_102.swf":
                game_name = "Papa's Cheeseria"
                lg = "cheese"
            if game_name == "papascupcakeria.swf":
                game_name = "Papa's Cupcakeria"
                lg = "cupcake"
            if game_name == "papasdonuteria.swf":
                game_name = "Papa's Donuteria"
                lg = "donut"
            if game_name == "papasfreezeria.swf":
                game_name = "Papa's Freezeria"
                lg = "freezeria"
            if game_name == "papashotdoggeria.swf":
                game_name = "Papa's Hot Doggeria"
                lg = "hotdog"
            if game_name == "papaspancakeria.swf":
                game_name = "Papa's Pancakeria"
                lg = "pancake"
            if game_name == "papaspastaria.swf":
                game_name = "Papa's Pastaria"
                lg = "pasta"
            if game_name == "papasscooperia_v102.swf":
                game_name = "Papa's Scooperia"
                lg = "scoop"
            if game_name == "papassushiria.swf":
                game_name = "Papa's Sushiria"
                lg = "sushi"
            if game_name == "papastacomia.swf":
                game_name = "Papa's Taco Mia!"
                lg = "taco"
    else: 
        game_name = "Adobe Flash"
        lg = "noflash"
# Initialize the RPC client with your application's client ID
client_id = "1122093746402627604"
RPC = Presence(client_id)
RPC.connect()

# Update the Rich Presence data
RPC.update(
    details="Playing" + " " + game_name,
    large_image=lg,
    small_image="flash",
    start=int(time.time())
)

# Keep the script running
while True:
    time.sleep(15)  # Update the presence every 15 seconds
    RPC.update(state="No game has been loaded yet.")

# Disconnect the RPC client when done
RPC.close()
