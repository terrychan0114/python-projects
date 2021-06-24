import RPi.GPIO as GPIO
import time

def button_handler(pin):
    print("pin %s's value is %s" % (pin, GPIO.input(pin)))

if __name__ == '__main__':
    button_pin = 10

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(button_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

    # events can be GPIO.RISING, GPIO.FALLING, or GPIO.BOTH
    GPIO.add_event_detect(button_pin, GPIO.BOTH,
                          callback=button_handler,
                          bouncetime=300)

    try:
        time.sleep(1000)
    except KeyboardInterrupt:
        GPIO.cleanup()