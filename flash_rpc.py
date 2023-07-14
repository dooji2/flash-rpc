# File: flash_rpc.py
# Project: flash-discord-RPC
# File Created: Saturday, ‎June ‎24, ‎2023, ‏‎10:26:38 AM
# Author: Dooji (doojisbasement@gmail.com)
# GitHub: https://github.com/dooji2
# Discord: dooji_

# Last Modified: ‎Tuesday, ‎July ‎4, ‎2023, ‏‎2:54:57 PM
# Modified By: Dooji (doojisbasement@gmail.com)

# Copyright (c) 2023 Dooji

import json
import os
import sys
import time
import threading

import psutil
import pystray
import tkinter as tk
from PIL import Image, ImageTk
from pypresence import Presence


if getattr(sys, "frozen", False):
    bundle_dir = sys._MEIPASS
else:
    bundle_dir = os.path.dirname(os.path.abspath(__file__))

icon_path = os.path.join(bundle_dir, "icon.png")
dooji_path = os.path.join(bundle_dir, "dooji.png")

GAME_INFO = ""
with open("game_info.json") as info_file:
    GAME_INFO = json.load(info_file)

client_id = "1122093746402627604"
RPC = Presence(client_id)
RPC.connect()


def recheck(game_name):

    for process in psutil.process_iter():

        # if the process _seems_ to be flash
        if "flash" in process.name():
            flash_command = " ".join(process.cmdline())

            # if we find the swf extension in the commandline used to start the process
            # we decide this is a flash process running a .swf game
            if ".swf" in flash_command:
                # assume the swf file is the last argument and extract that
                game_name = flash_command.split(os.path.sep)[-1]

                # match the swf file name to a database of known games
                for known_game_name in GAME_INFO.keys():
                    if game_name.lower() in known_game_name.lower():

                        # if we find a match, get the game details from the database and
                        # set them in discord with the RPC client
                        game_info = GAME_INFO[known_game_name]

                        RPC.update(
                            details=game_info["details"],
                            large_image=game_info["large_image"],
                            small_image=game_info["small_image"]
                            if "small_image" in game_info
                            else "flash",
                        )
            else:
                RPC.update(
                    details="Seems to be in Flash, idling...",
                    large_image="noflash",
                )


def run_script():
    while True:
        flash_found = False
        # Find the process of flash
        for process in psutil.process_iter():
            if "flash" in process.name():
                flash_found = True
                flash_command = " ".join(process.cmdline())
                # Look for a game file name in the process command line
                if "swf" in flash_command:
                    game_name = flash_command.split(os.path.sep)[-1]
                    # DO BLACK MAGICK
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

    about_window.eval("tk::PlaceWindow . center")

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
