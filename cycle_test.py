import RPi.GPIO as GPIO
import numpy as np
from time import sleep
import threading

class pushButtonTest:
    def __init__(self, open_pin, close_pin, button_pin, target_cycle, current_cycle):
        # Setting all of the corresponding device pins

        # Use the pin numbers as they appear on the board 
        GPIO.setmode(GPIO.BOARD) 
        GPIO.setup(open_pin, GPIO.OUT) #Red LED 
        GPIO.setup(close_pin, GPIO.OUT) #Yellow LED 
        GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
        GPIO.output(open_pin, False)
        GPIO.output(close_pin, False)

        # Setting target
        self.target_cycle = target_cycle
        self.current_cycle = current_cycle
        
    def reset_position(self):
        GPIO.output(open_pin, False)
        GPIO.output(close_pin, False)
        return
    
    def reset(self):
        self.reset_position()
        GPIO.cleanup()
        return
    
    def open_part(self):
        print("Opening part")
        GPIO.output(open_pin, True)
        sleep(4)
        GPIO.output(open_pin, False)
        sleep(3)
        return
    
    def close_part(self):
        print("Closing part")
        GPIO.output(close_pin, True)
        sleep(5)
        GPIO.output(close_pin, False)
        sleep(1)
        return
    
    def execute_test(self):
        self.reset_position()
        self.open_part()
        sleep(1)
#         self.close_part()
#         sleep(1)
        self.current_cycle += 1
        return
    
def button_thread(name):
    start_flag = False
    while True:
        if GPIO.input(10) == GPIO.HIGH:
            start_flag = np.invert(start_flag)
            logging.info("Button Thread: Flag: %b",start_flag)     

try:
    open_pin = 11
    close_pin = 13
    button_pin = 10
    target_cycle = 5000
    current_cycle = 4355
    
    start_flag = False
    
    cycle_test = pushButtonTest(open_pin, close_pin, button_pin, target_cycle, current_cycle)
    while start_flag == False:
        if GPIO.input(button_pin) == GPIO.HIGH:
            start_flag = True
            print("Cycle start")
    
    while (cycle_test.current_cycle <= cycle_test.target_cycle and start_flag):
        print("Current cycle is: ",cycle_test.current_cycle)
        cycle_test.execute_test()

    print("Cycle finished")
    GPIO.cleanup()
    
except KeyboardInterrupt:
    # cleanup the GPIO loose ends
    GPIO.cleanup()
