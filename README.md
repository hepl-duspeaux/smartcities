# Smartcities

Dans le cardre du projet Smartcities, nous devons d'abord prendre en main le raspberry pi Pico W et pour cela, nous faisons quelques petits projets. Ces projets nous permettent également de découvrir le langage de programation MicroPython.

## Raspberry pi Pico W

Le raspberry pi Pico W est le micro contrôleur qui nous permettra de faire le projet. Il a une fréquence de 133MHz et contrairement au Rpi Pico, il a le wifi et le bluetooth. Il a également 30 GPIO donc 3 ADC externes, 16 PWM, 2 UART, 2 I2C et 2 SPI.

![{01388CD3-4039-4D09-84CA-AFF12DEB8728}](https://github.com/user-attachments/assets/d6b2487e-b043-4f99-8f62-24570779dd64)

## MicroPython

Le python est un langage de programmation de haut niveau. Le MicroPython ressemble fortement au python mais il est adapté au micro contrôleur comme par exemple rpi et esp32. Par rapport au python, le MicroPython est aussi plus léger.

### IDE

Pour programmer, j'ai dû choisir un IDE et j'ai téléchargé Thonny. Thonny est un programme de développement gratuit qui permet de ne programmer que le python (micropython). Il est suffisant pour débuter car il intègre les outils et bibliothèque de base.

## Répertoires

[GPIO](GPIO): LED simple, bouton-poussoir, interruption.

[AD-PWM](AD-PWM): lecture du potentiomètre, PWM (LED, musique, servo).

[LCD](LCD): documentation des fonctions de la librairie, affichage de la valeur du potentiomètre.

[LED_neo](LED_neo): utilisation des LEDs néopixel, documentation des fonctions de la librairie, arc-en-ciel.

[sensors](sensors): température et humidité, luminosité, PIR

[network](network): accès réseaux avec le RPI Pico
