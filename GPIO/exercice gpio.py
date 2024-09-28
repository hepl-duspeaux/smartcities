import machine
import utime
from machine import Pin
LED = machine.Pin(16,machine.Pin.OUT)
BUTTON = machine.Pin(18,machine.Pin.IN)
value = 0


def fct_interruption(pin):

    global value
    value+=1
    
    print(value)
        
BUTTON.irq(trigger = Pin.IRQ_RISING, handler = fct_interruption)
#pin_button.irq(trigger=Pin.IRQ_FALLING,handler=button_isr)
while True:

    
    if value == 1:
        LED.value(1)
        utime.sleep(2)
        LED.value(0)
        utime.sleep(2)
        
    elif value == 2:
        LED.value(1)
        utime.sleep(1)
        LED.value(0)
        utime.sleep(1)
        
    elif value == 3:
        j=1
        while j<=500:
            LED.value(1)
            utime.sleep_ms(j)
            LED.value(0)
            utime.sleep_ms(j)
            j+=50
        
    elif value == 4:
        value =0
    