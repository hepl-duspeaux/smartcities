import machine, neopixel
from machine import I2C, Pin, ADC
from utime import sleep
from random import randint

p = machine.Pin.board.GP18
led = neopixel.NeoPixel(p, 1)
sound_sensor = ADC(1)
while True:
    average = 0
    for i in range (1000):
        noise = sound_sensor.read_u16()/256
        average += noise
    noise = average/1000
    print("noise: ",noise)
    if noise>45:
        for pixel_id in range(0, len(led)):
            red = randint(0,255)
            green = randint(0,255)
            blue = randint(0,255)
        # Assign the current LED a random red, green and blue value between 0 and 60
        led[pixel_id] = (red, green, blue)
        # Display the current pixel data on the Neopixel strip
        led.write()
            
   