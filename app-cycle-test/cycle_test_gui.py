import tkinter as tk
import requests
import json
import time
from loguru import logger
from tkinter.filedialog import askopenfilename, asksaveasfilename

server = 'http://localhost:8080/cycletest'

cycle_status = False

def call_for_status():
    global server
    try:
        r = requests.get('http://localhost:8080/cycletest')
        return_obj = r.json()
        if return_obj["cycle_status"] == False:
            logger.info("Successfully got info")
            logger.info("The cylinders are free")
            return True
        else: 
            logger.info("Successfully got info")
            logger.info("The cylinders are in use")
            return False
    except:
        logger.info("Something went wrong, can't connect to server")

def execute_cycle():
    global server
    try:
        status = call_for_status()
        while status == False:
            time.sleep(1)
            status = call_for_status()
        # Need to have the proper POST function
        requests.post('http://localhost:8080/cycletest')
        return
    except:
        logger.error("Not able to send in post request")
        raise

def start_cycle():
    start_number = ent_start_number.get()
    target_number = ent_target_number.get()
    current_number = start_number
    while current_number <= target_number:
        logger.info("Executing cycle number", current_number)
        execute_cycle()
        current_number += 1

# Create a new window with the title "Simple Text Editor"
window = tk.Tk()
window.title("Cycle test")

# Set row and column configuration
window.rowconfigure(0, minsize=100, weight=1)
window.columnconfigure(1, minsize=100, weight=1)

# Creating all of the widget components in this application
cycle_number = tk.Label(master=window, text="Input cycle start number and target number, then press start")

fr_entry = tk.Frame(window)
start_label = tk.Label(master=fr_entry, text="Start cycle number")
target_label = tk.Label(master=fr_entry, text="Target cyce number")
ent_start_number = tk.Entry(master=fr_entry, width=10)
ent_target_number = tk.Entry(master=fr_entry, width=10)


fr_btn = tk.Frame(window)
btn_start = tk.Button(fr_btn, text="Start")
btn_end = tk.Button(fr_btn, text="Stop")


# Arranging the widgets
start_label.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
target_label.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
start_number.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
target_number.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
btn_start.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_end.grid(row=0, column=1, sticky="ew", padx=5)
fr_entry.grid(row=0, column=0, sticky="ns")
fr_btn.grid(row=1, column=1, sticky="ns")
cycle_number.grid(row=0,column=1,sticky="nsew")
# Run windows
window.mainloop()