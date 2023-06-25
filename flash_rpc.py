# File: flash_rpc.py
# Project: flash-discord-RPC
# File Created: Saturday, ‎June ‎24, ‎2023, ‏‎10:26:38 AM
# Author: Dooji (doojisbasement@gmail.com)
# GitHub: https://github.com/dooji2
# Discord: dooji_

# Last Modified: ‎Sunday, ‎June ‎25, ‎2023, ‏‎3:13:10 PM
# Modified By: Dooji (doojisbasement@gmail.com)

# Copyright (c) 2023 Dooji
import time
import os
import psutil
from pypresence import Presence
import pystray
from PIL import Image
import threading
import sys
import ctypes
import base64
import tempfile


if getattr(sys, 'frozen', False):
    # The application is running in a bundle
    bundle_dir = sys._MEIPASS
else:
    # The application is running in the normal Python environment
    bundle_dir = os.path.dirname(os.path.abspath(__file__))

icon_path = os.path.join(bundle_dir, "icon.png")


client_id = "1122093746402627604"
RPC = Presence(client_id)
RPC.connect()

for process in psutil.process_iter():
        if "flash" in process.name(): 
            
            flash_command = " ".join(process.cmdline())
            if "swf" in flash_command:
                game_name = flash_command.split(os.path.sep)[-1]

def recheck(game_name):
    for process in psutil.process_iter():
        if "flash" in process.name(): 
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

def on_quit_callback(icon, item):
    icon.stop()
    RPC.close()
    print("Script stopped.")

def run_script():
    while True:
        if "flash" not in process.name(): 
            RPC.clear()
        if "flash" in process.name():
            recheck(game_name)
        time.sleep(5)  

def create_system_tray_icon():
    image = Image.open(icon_path)
    menu = (
        pystray.MenuItem("Exit Flash RPC", on_quit_callback),
    )
    icon = pystray.Icon("Flash RPC", image, "Flash RPC", menu)
    return icon

if __name__ == "__main__":
    icon = create_system_tray_icon()
    thread = threading.Thread(target=run_script)
    thread.start()
    icon.run()

