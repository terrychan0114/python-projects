import connexion
import six
import RPi.GPIO as GPIO

from server.models.cycle_test_info import CycleTestInfo  # noqa: E501
from server import util

cycle_status=False
init_status=False

def initialize_gpio():
    open_pin = 11
    close_pin = 13
    button_pin = 10
    GPIO.setmode(GPIO.BOARD) 
    GPIO.setup(open_pin, GPIO.OUT) #Red LED 
    GPIO.setup(close_pin, GPIO.OUT) #Yellow LED 
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    GPIO.output(open_pin, False)
    GPIO.output(close_pin, False)
# This function is to get the pi status
def pi_status():
    # This is the function to test if the test is still running
    print("Cycle is running")
    return

def open_latch():

    return
def close_latch():
    return

def run_cycle():
    global cycle_status
    cycle_status = True
    open_latch()
    close_latch()
    return 

def get_cycle():  # noqa: E501
    """Get the information

     # noqa: E501


    :rtype: List[CycleTestInfo]
    """
    return 'do some magic!'


def start_cycle(body):  # noqa: E501
    """Add a new info to the server

     # noqa: E501

    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = CycleTestInfo.from_dict(connexion.request.get_json())  # noqa: E501
    part_number = body.part_number
    cycle_number = body.cycle_number
    return 'do some magic!'
