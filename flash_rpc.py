# File: flash_rpc.py
# Project: flash-discord-RPC
# File Created: Saturday, ‎June ‎24, ‎2023, ‏‎10:26:38 AM
# Author: Dooji (doojisbasement@gmail.com)
# GitHub: https://github.com/dooji2
# Discord: dooji_

# Last Modified: ‎Tuesday, ‎July ‎4, ‎2023, ‏‎2:39:39 PM
# Modified By: Dooji (doojisbasement@gmail.com)

# Copyright (c) 2023 Dooji
import time
import os
import psutil
from pypresence import Presence
import pystray
from PIL import Image, ImageTk
import threading
import sys
import ctypes
import base64
import tempfile
import asyncio
import tkinter as tk
from tkinter import messagebox
from queue import Queue

if getattr(sys, 'frozen', False):
    bundle_dir = sys._MEIPASS
else:
    bundle_dir = os.path.dirname(os.path.abspath(__file__))

icon_path = os.path.join(bundle_dir, "icon.png")
dooji_path = os.path.join(bundle_dir, "dooji.png")

client_id = "1122093746402627604"
RPC = Presence(client_id)
RPC.connect()

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
                elif "pacman" in game_name.lower():
                    RPC.update(details="Playing Pac-Man", large_image="pacman", small_image="flash")
                elif "fireboy" in game_name.lower() or "watergirl" in game_name.lower():
                    RPC.update(details="Playing Fireboy and Watergirl", large_image="fandw", small_image="flash")
                #
                #
                #
                elif "supermario" in game_name:
                    RPC.update(details="Playing Super Mario Flash", large_image="supermario", small_image="flash")
                elif "arkanoid" in game_name:
                    RPC.update(details="Playing Arkanoid", large_image="arkanoid", small_image="flash")
                elif "tetris" in game_name:
                    RPC.update(details="Playing Tetris", large_image="tetris", small_image="flash")
                elif "snake" in game_name:
                    RPC.update(details="Playing Snake", large_image="snake", small_image="flash")
                elif "minesweeper" in game_name:
                    RPC.update(details="Playing Minesweeper", large_image="minesweeper", small_image="flash")
                elif "solitaire" in game_name:
                    RPC.update(details="Playing Solitaire", large_image="solitaire", small_image="flash")
                elif "sudoku" in game_name:
                    RPC.update(details="Playing Sudoku", large_image="sudoku", small_image="flash")
                elif "bejeweled" in game_name:
                    RPC.update(details="Playing Bejeweled", large_image="bejeweled", small_image="flash")
                elif "2048" in game_name:
                    RPC.update(details="Playing 2048", large_image="2048", small_image="flash")
                elif "angrybirds" in game_name:
                    RPC.update(details="Playing Angry Birds", large_image="angrybirds", small_image="flash")
                elif "plantsvszombies" in game_name:
                    RPC.update(details="Playing Plants vs. Zombies", large_image="plantsvszombies", small_image="flash")
                elif "cuttherope" in game_name:
                    RPC.update(details="Playing Cut the Rope", large_image="cuttherope", small_image="flash")
                elif "bloonstd" in game_name:
                    RPC.update(details="Playing Bloons TD", large_image="bloonstd", small_image="flash")
                elif "happywheels" in game_name:
                    RPC.update(details="Playing Happy Wheels", large_image="happywheels", small_image="flash")
                elif "flappybird" in game_name:
                    RPC.update(details="Playing Flappy Bird", large_image="flappybird", small_image="flash")
                elif "penguin" in game_name:
                    RPC.update(details="Playing Learn to Fly", large_image="penguin", small_image="flash")
                elif "raftwars" in game_name:
                    RPC.update(details="Playing Raft Wars", large_image="raftwars", small_image="flash")
                elif "ageofwar" in game_name:
                    RPC.update(details="Playing Age of War", large_image="ageofwar", small_image="flash")
                elif "stickwar" in game_name:
                    RPC.update(details="Playing Stick War", large_image="stickwar", small_image="flash")
                elif "linegame" in game_name:
                    RPC.update(details="Playing The Line Game", large_image="linegame", small_image="flash")
                elif "happyroom" in game_name:
                    RPC.update(details="Playing Happy Room", large_image="happyroom", small_image="flash")
                elif "bighouseclean" in game_name:
                    RPC.update(details="Playing Big House Clean Up", large_image="bighouseclean", small_image="flash")
                elif "boxhead" in game_name:
                    RPC.update(details="Playing Boxhead", large_image="boxhead", small_image="flash")
                elif "defendyourcastle" in game_name:
                    RPC.update(details="Playing Defend Your Castle", large_image="defendyourcastle", small_image="flash")
                elif "portal" in game_name:
                    RPC.update(details="Playing Portal: The Flash Version", large_image="portal", small_image="flash")
                elif "maxdamage" in game_name:
                    RPC.update(details="Playing Max Damage", large_image="maxdamage", small_image="flash")
                elif "neonrider" in game_name:
                    RPC.update(details="Playing Neon Rider", large_image="neonrider", small_image="flash")
def run_script():
    while True:
        flash_found = False
        for process in psutil.process_iter():
            if "flash" in process.name():
                flash_found = True
                flash_command = " ".join(process.cmdline())
                if "swf" in flash_command:
                    game_name = flash_command.split(os.path.sep)[-1]
                    recheck(game_name)
                    break

        if not flash_found:
            RPC.clear()
        if "flash" in process.name():
            recheck(game_name)
        time.sleep(5)  

# def create_about_window():
#     about_window = tk.Toplevel()
#     about_window.title("About Flash RPC")
#     about_window.geometry("300x200")

#     
#     icon_image = Image.open(dooji_path)
#     icon_image = icon_image.resize((100, 100))  
#     icon_photo = ImageTk.PhotoImage(icon_image)
#     icon_label = tk.Label(about_window, image=icon_photo)
#     icon_label.pack(pady=20)

#     
#     credits_label = tk.Label(about_window, text="Author: Dooji\nVersion: 1.0")
#     credits_label.pack()

#     
#     about_window.deiconify()

def on_quit_callback(icon):
    icon.stop()
    RPC.close()
    os._exit(0)


def create_about_window():
    about_window = tk.Tk()
    about_window.title("About Flash RPC")
    about_window.geometry("300x200")
    about_window.resizable(False, False)  

    imagei = Image.open(dooji_path)
    imagei = imagei.resize((100, 100), Image.LANCZOS)
    photo = ImageTk.PhotoImage(imagei)

    label = tk.Label(about_window, image=photo)
    label.imagei = photo  
    label.pack(pady=20)

    credits_label = tk.Label(about_window, text="Author: Dooji\nVersion: 1.0.5")
    credits_label.pack()

    about_window.eval('tk::PlaceWindow . center')

    about_window.mainloop()

def create_system_tray_icon():
    image = Image.open(icon_path)

    menu = (
        pystray.MenuItem(
            "About",
            lambda: create_about_window(),
        ),
        pystray.MenuItem("Exit Flash RPC", on_quit_callback),
    )

    icon = pystray.Icon("Flash RPC", image, "Flash RPC", menu)
    return icon

if __name__ == "__main__":
    icon = create_system_tray_icon()

    rpc_thread = threading.Thread(target=run_script)
    rpc_thread.start()

    icon.run()