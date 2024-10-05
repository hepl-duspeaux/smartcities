from machine import Pin, PWM, ADC, Timer
import utime
buzzer = PWM(Pin(18))
rotary_angle_sensor = ADC(0)


def interrupt(timer):
    
    buzzer.duty_u16(rotary_angle_sensor.read_u16())
    

Timer().init(freq=100, mode=Timer.PERIODIC, callback=interrupt)
    
def do():
    buzzer.freq(1046)
    
def re():
    buzzer.freq(1175)
    
def mi():
    buzzer.freq(1318)
    
def fa():
    buzzer.freq(1397)
    
def sol():
    buzzer.freq(1568)
    
def la():
    buzzer.freq(1760)
    
def si():
    buzzer.freq(1967)
    
def n():
    buzzer.duty_u16(10) #close
    
while True:
    la()
    utime.sleep_ms(250)
    do()
    utime.sleep_ms(250)
    re()
    utime.sleep_ms(500)
    re()
    utime.sleep_ms(500)
    re()
    utime.sleep_ms(250)
    mi()
    utime.sleep_ms(250)
    fa()
    utime.sleep_ms(500)
    fa()
    utime.sleep_ms(500)
    fa()
    utime.sleep_ms(250)
    sol()
    utime.sleep_ms(250)
    mi()
    utime.sleep_ms(500)
    mi()
    utime.sleep_ms(500)
    re()
    utime.sleep_ms(250)
    do()
    utime.sleep_ms(250)
    re()
    utime.sleep_ms(1000)
    la()
    utime.sleep_ms(250)
    do()
    utime.sleep_ms(250)
    re()
    utime.sleep_ms(500)
    re()
    utime.sleep_ms(500)
    re()
    utime.sleep_ms(250)
    fa()
    utime.sleep_ms(250)
    sol()
    utime.sleep_ms(500)
    sol()
    utime.sleep_ms(500)
    sol()
    utime.sleep_ms(250)
    la()
    utime.sleep_ms(250)
    
    