from lcd1602 import LCD1602
from dht11 import *
from machine import I2C,Pin,ADC,PWM, Timer
from utime import sleep

i2c = I2C(1,scl=Pin(7), sda=Pin(6), freq=400000)
d = LCD1602(i2c, 2, 16)
d.display()
LED = machine.Pin(20,machine.Pin.OUT)
dht = DHT(18)
ROTARY_ANGLE_SENSOR = ADC(0)
buzzer = PWM(Pin(16))
buzzer.freq(500)
start0 = time.ticks_ms()# start pour DHT11
start1 = time.ticks_ms()# start pour raffraichissement LCD
start2 = time.ticks_ms()# start pour ADC
temp=0
set=0
set3 =0
LED.value(0)

while True:
    
    if time.ticks_diff(time.ticks_ms(), start0) > 1000:      
        temp,humid = dht.readTempHumid()
        start0 = time.ticks_ms()
        
    if time.ticks_diff(time.ticks_ms(), start1) > 100:
        d.clear()
        d.setCursor(0,0)
        if temp >= set3:
            d.print("ALARM")
        else:
            d.print("Set: "+str(set))
        d.setCursor(0,1)
        d.print("Ambient: "+str(temp))
        start1 = time.ticks_ms()
        
    if time.ticks_diff(time.ticks_ms(), start2) > 200:
        set=(((ROTARY_ANGLE_SENSOR.read_u16())/65535)*20)+15
        set= round(set,2)
        start2 = time.ticks_ms()
    
    set3 = set + 3
    if temp > set and temp < set3:
        LED.value(not LED.value())
        sleep(2)

    if temp >= set3:
        LED.value(not LED.value())
        sleep(0.5)
        buzzer.duty_u16(33000)
    else:
        LED.value(0)
        buzzer.duty_u16(0)
    