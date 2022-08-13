from machine import Pin
import time

led = Pin(25, Pin.OUT)
state = Pin(13, Pin.IN, Pin.PULL_UP)
while True:
    time.sleep(1)
    if state.value() == 1:
        led.value(1)
        print("ON")
    else:
        led.value(0)
        print("OFF")
    
