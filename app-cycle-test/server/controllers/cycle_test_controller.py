import connexion
import six
import sys
# import RPi.GPIO as GPIO
from loguru import logger
from time import sleep
from server.models.cycle_test_info import CycleTestInfo  # noqa: E501
from server import util
from threading import *
import datetime

# cycle_status == False --> Ready to use
# cycle_status == True --> In use
cycle_status=False

init_status=False
cycle_number = 0
part_number = ""
open_pin = 11
close_pin = 13

test = False

def initialize_gpio():
    logger.info("Initializing GPIO ports")
    global open_pin
    global close_pin

    try:
        GPIO.setmode(GPIO.BOARD) 
        GPIO.setup(open_pin, GPIO.OUT) #Red LED 
        GPIO.setup(close_pin, GPIO.OUT) #Yellow LED 
        GPIO.output(open_pin, False)
        GPIO.output(close_pin, False)
        logger.info("Successful initialization")
        global init_state
        init_state = True
    except:
        logger.info("Initilization failed")
    return

# This function is to get the pi status
def pi_status():
    # This is the function to test if the test is still running
    global cycle_status
    if cycle_status == False:
        logger.info("The cycle is not running")
        return False
    else:
        logger.info("The cycle is running")
        return True

def open_latch():
    global open_pin
    global close_pin
    logger.info("Opening part")
    # GPIO.output(open_pin, True)
    sleep(4)
    # GPIO.output(open_pin, False)
    sleep(3)
    return

def close_latch():
    global open_pin
    global close_pin
    logger.info("Closing part")
    # GPIO.output(close_pin, True)
    sleep(10)
    # GPIO.output(close_pin, False)
    sleep(1)
    return

def full_cycle():
    global cycle_status
    cycle_status = True
    open_latch()
    close_latch()
    logger.info("Cycle finished")
    cycle_status = False
    sys.exit()
    return

def full_cycle_thread():
    global cycle_status
    logger.debug("Starting cycle thread")
    t1 = Thread(target = full_cycle)
    t1.start()

def run_cycle():
    global cycle_status
    global init_status
    cycle_status = True
    try:
        if init_status == False:
            logger.info("Require initilization")
            initialize_gpio()
        logger.info("Starting test")
        logger.info("Open latch")
        open_latch()
        logger.info("Close latch")
        close_latch()
        cycle_status = False
        return True
    except:
        logger.error("Something went wrong...")
        cycle_status = False
        return False

def get_cycle():  # noqa: E501
    """Get the information

     # noqa: E501


    :rtype: CycleTestInfo
    """
    global cycle_status
    try:
        logger.info("Getting current info")
        return_obj = CycleTestInfo()
        return_obj.cycle_status = cycle_status
        return_obj.date = datetime.datetime.now()
    except:
        logger.error("Failed to get info")
    return return_obj


def start_cycle(body):  # noqa: E501
    """Add a new info to the server

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = CycleTestInfo.from_dict(connexion.request.get_json())  # noqa: E501
    logger.info("Got trigger signal")
    # full_cycle_thread()
    return "Let's dance"
