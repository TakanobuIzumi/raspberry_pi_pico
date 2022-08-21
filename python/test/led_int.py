import machine
from machine import Pin
import time

def callback(pin):
#    iqr_state = machine.disable_irq()
    global sw_int
    global sw_value
    sw_int = True
    if sw_value == 'off':
        sw_value = 'on'
        print("Btn!On")
    else:
        sw_value = 'off'
        print("Btn!Off")
#    machine.enable_irq(iqr_state)　

def main():
    global sw_int
    global sw_value
    sw_int = None
    sw_value = 'off'
    led = Pin(25, Pin.OUT)
    state = Pin(13, Pin.IN, Pin.PULL_UP)

    state.irq(trigger=Pin.IRQ_FALLING, handler=callback)

    while True:
        if sw_int:
            if sw_value == 'on':
                led.value(1)
            else:
                led.value(0)
            sw_int = None
        
if __name__ == "__main__":
   main()
   