from gpiozero import LED, Button
from time import sleep

heavy_piston = LED(17)
light_piston = LED(27)
button = Button(2)
current_cycle = 1
cycle_target = 1000

def open_latch():
    light_piston.on()
    sleep(2)
    light_piston.off()
    sleep(1)

def close_latch():
    heavy_piston.on()
    sleep(3)
    heavy_piston.off()
    sleep(1)

def initialize():
    heavy_piston.off()
    light_piston.off()
    
def execution():
    # This is the execution of a cycle
    initialize()
    open_latch()
    sleep(1)
    close_latch()
    sleep(1)

def main():
    initialize()
    while True:
        if button.is_pressed:
            print("Cycle start")
            while current_cycle <= cycle_target:
                execution()
                current_cycle += 1

main()
    