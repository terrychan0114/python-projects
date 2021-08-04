import connexion
import six
import sys
import RPi.GPIO as GPIO
from loguru import logger
from time import sleep
from server.models.cycle_test_info import CycleTestInfo  # noqa: E501
from server import util
from threading import *
import datetime

# cycle_status == False --> Ready to use
# cycle_status == True --> In use
cycle_status=False
stop_flag = False
init_status=False
cycle_number = 0
open_pin = 11
close_pin = 13

def initialize_gpio():
    logger.info("Initializing GPIO ports")
    global open_pin
    global close_pin
    #try:
    #    GPIO.cleanup()
    #    logger.debug("GPIO  cleaned up")
    #except:
    #    logger.debug("GPIO already cleaned up")
    try:
        GPIO.setmode(GPIO.BOARD) 
        GPIO.setup(open_pin, GPIO.OUT, initial=GPIO.LOW) #Red LED 
        GPIO.setup(close_pin, GPIO.OUT, initial=GPIO.LOW) #Yellow LED 
        GPIO.output(open_pin, False)
        GPIO.output(close_pin, False)
        # # Check if initialization is completed:
        # open_channel_is_on = GPIO.input(open_pin)
        # close_channel_is_on = GPIO.input(close_pin)
        # if (open_channel_is_on and close_channel_is_on):
        #     logger.info("Successful initialization") 
        #     global init_status
        #     init_status = True
        # else:
        #     logger.debug(f"open channel is {open_channel_is_on}")
        #     logger.debug(f"close channel is {close_channel_is_on}")
        #     logger.error("Initialization not completed")
    except:
        logger.info("Init startup failed")
    return

# This function is to get the pi status
def pi_status():
    # This is the function to test if the test is still running
    global cycle_status
    if cycle_status == False:
        # logger.debug("The cycle is not running")
        return False
    else:
        # logger.debug("The cycle is running")
        return True

def open_latch():
    global open_pin
    global close_pin
    logger.info("Opening part")
    GPIO.output(open_pin, True)
    sleep(4)
    GPIO.output(open_pin, False)
    sleep(3)
    return

def close_latch():
    global open_pin
    global close_pin
    logger.info("Closing part")
    GPIO.output(close_pin, True)
    sleep(10)
    GPIO.output(close_pin, False)
    sleep(1)
    return

def full_cycle():
    global cycle_status
    global stop_flag
    operation = 0
    if stop_flag == False:
        open_latch()
        operation += 1
    else:
        # logger.info("Cycle stopped")
        logger.info("Closing execute cycle thread on open")

        return
    if stop_flag == False:
        close_latch()
        operation += 1
    else: 
        # logger.info("Cycle stopped")
        logger.info("Closing execute cycle thread on close")

        return
    if operation == 2:
        logger.info("Cycle finished")
    else: 
        logger.info("Cycle stopped")
    cycle_status = False
    sys.exit()
    return

def full_cycle_thread():
    global cycle_status
    cycle_status = True
    logger.debug("Start execute cycle thread")
    t1 = Thread(target = full_cycle)
    t1.start()

def reset_thread():

    global stop_flag
    global cycle_status
    while cycle_status == True:
        logger.debug("Still in use")
        sleep(1)
    GPIO.cleanup()
    logger.debug("Cleanup finished")
    logger.debug("Closing reset thread")
    sys.exit()
    return

def get_cycle():  # noqa: E501
    """Get the information

     # noqa: E501

    :rtype: CycleTestInfo
    """
    global cycle_status
    try:
        # logger.info("Getting current info")
        return_obj = CycleTestInfo()
        return_obj.cycle_status = cycle_status
        return_obj.date = datetime.datetime.now()
    except:
        logger.error("Failed to get info")
    return return_obj

def reset_gpio():  # noqa: E501
    """This is to reset the system and GPIO port

     # noqa: E501

    :rtype: None
    """
    global cycle_status
    global stop_flag
    stop_flag = True
    logger.debug("Starting reset thread")
    t2 = Thread(target = reset_thread)
    t2.start()
    return "",200

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
    global init_status
    global stop_flag
    if init_status == False:
        logger.info("Initializing GPIO")
        initialize_gpio()
    stop_flag = False
    full_cycle_thread()
    return "", 200
