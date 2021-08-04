import tkinter as tk
import requests
import json
import time
import sys
from loguru import logger
from threading import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

server_addr = 'http://localhost:8080'

cycle_status = False
stop_flag = False

def call_for_status():
    global server_addr
    try:

        r = requests.get(server_addr+'/cycletest')
        return_obj = r.json()
        if return_obj["cycle_status"] == False:
            # logger.debug("Successfully got info")
            # logger.debug("The cylinders are free")
            return True
        else: 
            # logger.debug("Successfully got info")
            # logger.debug("The cylinders are in use")
            return False
    except:
        logger.error("Cannot connect to server")

def start_cycle_thread():
    logger.debug("Starting cycle thread")
    t1 = Thread(target=start_cycle)
    t1.start()

def execute_cycle():
    global server_addr
    try:
        status = call_for_status()
        while status == False:
            time.sleep(1)
            logger.info("The pistons are in use, please wait")
            status = call_for_status()
        # Need to have the proper POST function
        if stop_flag == False:
            logger.info("Now sending executing signal to piston server")
            # send over the signal to the server
            payload = {
                'cycle_status': True
            }
            r = requests.post(server_addr+'/cycletest',json=payload)
            if r.status_code == 200:
                logger.debug("Request ok")
            elif r.status_code == 415:
                logger.error("Unsupported payload")
            elif r.status_code == 400:
                logger.error("Bad request")
            else: 
                logger.error("Something is wrong")
            time.sleep(1)
            return
        else:
            return
    except:
        logger.error("Not able to send in post request")
        raise

def start_cycle():
    
    try:
        start_number = int(ent_start_number.get())
    except ValueError:
        logger.error("Entry value is not an integer")
        cycle_number["text"] = "Start number is not integer"
    try:
        target_number = int(ent_target_number.get())
    except ValueError:
        logger.error("Entry value is not an integer")
        cycle_number["text"] = "Target number is not integer"
    current_number = start_number
    while current_number <= target_number:
        global stop_flag
        if stop_flag == False:
            logger.info(f"Executing cycle #{current_number}")
            cycle_number["text"] = f"Executing cycle {current_number}"
            execute_cycle()
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
    reset_gpio()

def reset_gpio():
    r = requests.get(server_addr+'/reset')
    if r.status_code == 200:
        logger.info("GPIO reset finished")
    else:
        logger.error("GPIO reset failed")

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
target_label = tk.Label(master=fr_entry, text="Target cycle number")
ent_start_number = tk.Entry(master=fr_entry, width=10)
ent_target_number = tk.Entry(master=fr_entry, width=10)

fr_btn = tk.Frame(window)
btn_start = tk.Button(fr_btn, text="Start",command=start_cycle_thread)
btn_end = tk.Button(fr_btn, text="Stop",command=stop_cycle)
# btn_reset = tk.Button(fr_btn,text="Reset",command=reset)

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