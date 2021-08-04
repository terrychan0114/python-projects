from tkinter import *
import time
import json
from threading import *
import requests
import datetime
import GPIO
from loguru import logger

open_pin = 11
close_pin = 13

GPIO.setmode(GPIO.BOARD) 
GPIO.setup(open_pin, GPIO.OUT) #Red LED 
GPIO.setup(close_pin, GPIO.OUT) #Yellow LED 
GPIO.output(open_pin, False)
GPIO.output(close_pin, False)
# Check if initialization is completed:
open_channel_is_on = GPIO.input(open_pin)
close_channel_is_on = GPIO.input(close_pin)
if (open_channel_is_on and close_channel_is_on):
    logger.info("Successful initialization") 
    global init_status
    init_status = True
else:
    logger.debug(f"open channel is {open_channel_is_on}")
    logger.debug(f"close channel is {close_channel_is_on}")
    logger.error("Initialization not completed")