"""
Test de l'ADC et du PWM
Le code permet de modifier le duty cycle du PWM en fonction de l'angle
du potentiomètre rotatif.
"""
from machine import Pin, ADC, PWM

rotary_angle_sensor = ADC(0)
led_PWM = PWM(Pin(18))

led_PWM.freq(500)

while True:
    val = rotary_angle_sensor.read_u16()
    led_PWM.duty_u16(val)

