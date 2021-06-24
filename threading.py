import logging
import threading
import numpy as np
import time
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library


# GPIO.setwarnings(False) # Ignore warning for now
# GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
# GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
# global start_flag
start_flag = False

def button_handler(channel):
    start_flag = np.invert(start_flag)
    logging.info("Button Thread: Flag: ",start_flag)
# 
# def button_thread():
#     while True:
#         GPIO.add_event_detect(10, GPIO.RISING,
#                               callback=button_handler,
#                               bouncetime=300)        

if __name__ == "__main__":
    GPIO.setwarnings(False) # Ignore warning for now
    GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
    GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
    
    start_flag = False
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
#     x = threading.Thread(target=button_thread)
#     logging.info("Main    : before running thread")
#     x.start()
    GPIO.add_event_detect(10, GPIO.RISING,
                          callback=button_handler,
                          bouncetime=300)      
    for i in range(0,10):
        try:
#             while start_flag == True:
                logging.info("Main: Counting number: %d",i)
                time.sleep(2)
        except KeyboardInterrupt:
            logging.info("Keyboard interrupt")
    #x.join()
    logging.info("Main    : all done")