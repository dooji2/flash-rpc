# File: flash_rpc.py
# Project: flash-discord-RPC
# File Created: Saturday, ‎June ‎24, ‎2023, ‏‎10:26:38 AM
# Author: Dooji (doojisbasement@gmail.com)
# GitHub: https://github.com/dooji2
# Discord: dooji_

# Last Modified: ‎Sunday, ‎June ‎25, ‎2023, ‏‎4:47:37 PM
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
import tkinter as tk
from tkinter import messagebox
from queue import Queue

if getattr(sys, 'frozen', False):
    # The application is running in a bundle
    bundle_dir = sys._MEIPASS
else:
    # The application is running in the normal Python environment
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
        try:
            time.sleep(5)
        except KeyboardInterrupt:
            break

# def create_about_window():
#     about_window = tk.Toplevel()
#     about_window.title("About Flash RPC")
#     about_window.geometry("300x200")

#     # Load and display the icon image
#     icon_image = Image.open(dooji_path)
#     icon_image = icon_image.resize((100, 100))  # Adjust the size as needed
#     icon_photo = ImageTk.PhotoImage(icon_image)
#     icon_label = tk.Label(about_window, image=icon_photo)
#     icon_label.pack(pady=20)

#     # Display the program credits
#     credits_label = tk.Label(about_window, text="Author: Dooji\nVersion: 1.0")
#     credits_label.pack()

#     # Make the about window visible
#     about_window.deiconify()

def on_quit_callback(icon):
    icon.stop()
    RPC.close()
    rpc_thread.join()  # Wait for the rpc_thread to finish
    try:
        sys.exit()  # Exit the Python interpreter
    except SystemExit:
        pass

def create_about_window():
    about_window = tk.Tk()
    about_window.title("About Flash RPC")
    about_window.geometry("300x200")
    about_window.resizable(False, False)  # Disable window resizing

    # Load and resize the image
    image = Image.open(dooji_path)
    image = image.resize((100, 100), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
    label = tk.Label(about_window, image=photo)
    label.image = photo  # Keep a reference to prevent image from being garbage collected
    label.pack(pady=20)

    # Display the program credits
    credits_label = tk.Label(about_window, text="Author: Dooji\nVersion: 1.0.3c")
    credits_label.pack()

    # Center the window on the screen
    about_window.eval('tk::PlaceWindow . center')

    # Start the Tkinter event loop for the about window
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

    # Start the RPC thread
    rpc_thread = threading.Thread(target=run_script)
    rpc_thread.start()

    # Run the system tray icon
    icon.run()