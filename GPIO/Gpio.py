import machine
import utime

LED = machine.Pin(16,machine.Pin.OUT)
BUTTON = machine.Pin(18,machine.Pin.IN)
val = 0


while True:

    if BUTTON.value() == 1:
        val = val+1
        utime.sleep(0.25)
    elif val == 2:
        val =0
        utime.sleep(0.25)
    LED.value(val)