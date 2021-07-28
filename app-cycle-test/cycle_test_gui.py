import tkinter as tk
import requests
import json
import time
import sys
from loguru import logger
from threading import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

server = 'http://localhost:8080/cycletest'

cycle_status = False
stop_flag = False
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

def start_cycle_thread():
    t1 = Thread(target=start_cycle)
    t1.start()

def execute_cycle():
    global server
    try:
        status = call_for_status()
        while status == False:
            time.sleep(1)
            status = call_for_status()
        # Need to have the proper POST function
        # requests.post('http://localhost:8080/cycletest')
        time.sleep(1)
        return
    except:
        logger.error("Not able to send in post request")
        raise

def start_cycle():
    global stop_flag
    try:
        start_number = int(ent_start_number.get())
    except ValueError:
        logger.error("Entry value is not an integer")
    try:
        target_number = int(ent_target_number.get())
    except ValueError:
        logger.error("Entry value is not an integer")
    current_number = start_number
    while current_number <= target_number:
        if stop_flag == False:
            logger.info("Executing cycle number", current_number)
            execute_cycle()
            cycle_number["text"] = f"Executing cycle {current_number}"
            current_number += 1
        else:
            logger.info("Stopping thread...")
            stop_flag = False
            cycle_number["text"] = f"Stopped at cycle {current_number-1}"
            sys.exit()
    cycle_number["text"] = f"Finished execution of {current_number-1} cycles"

def stop_cycle():
    global stop_flag
    stop_flag = True

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
btn_start = tk.Button(fr_btn, text="Start",command=start_cycle_thread)
btn_end = tk.Button(fr_btn, text="Stop",command=stop_cycle)


# Arranging the widgets
start_label.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
target_label.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
ent_start_number.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
ent_target_number.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
btn_start.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_end.grid(row=0, column=1, sticky="ew", padx=5)
fr_entry.grid(row=0, column=0, sticky="ns")
fr_btn.grid(row=1, column=1, sticky="ns")
cycle_number.grid(row=0,column=1,sticky="nsew")
# Run windows
window.mainloop()