from machine import Pin,Timer
import time

led = Pin(25, Pin.OUT)
state = Pin(13, Pin.IN, Pin.PULL_UP)

timer = Timer()

def tica2(timer):
    if state.value() == 1:
        led.value(1)
        print("ON")
    else:
        led.value(0)
        print("OFF")
        
timer.init(freq=10, mode=Timer.PERIODIC, callback=tica2)