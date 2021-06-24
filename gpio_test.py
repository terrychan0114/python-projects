#!/usr/bin/python 
import RPi.GPIO as GPIO 
import time

# Setup the GPIO ports 
light_piston = 11
heavy_piston = 13
button = 3
# Use the pin numbers as they appear on the board 
GPIO.setmode(GPIO.BOARD)

GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)
GPIO.setup(light_piston, GPIO.OUT) #Red LED 
GPIO.setup(heavy_piston, GPIO.OUT) #Yellow LED 

GPIO.output(light_piston, False)
GPIO.output(heavy_piston, False)

while True:
# Run 5 times
    if GPIO.input(button) == GPIO.HIGH:
        print("Button was pushed!")
        try:

          for i in range(0,5):
            # Each cycle should:
            # 1.  make the stoplight green for 5 seconds
            # 2.  turn the light yellow for 1 second
            # 3.  turn the light red for 5 seconds

            # turn the red light off and green light on
            GPIO.output(light_piston, False)
            GPIO.output(heavy_piston, True)
            # wait 5 seconds
            time.sleep(5)

            # turn the yellow light off and the red light on
            GPIO.output(heavy_piston, False)
            GPIO.output(light_piston, True)
            # wait 5 seconds
            time.sleep(5)

          # cleanup the GPIO loose ends
          GPIO.cleanup()

        except KeyboardInterrupt:
          # cleanup the GPIO loose ends
          GPIO.cleanup()
