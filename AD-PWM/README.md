# Exercice 2: volume d'une mélodie

Créer un programme MicroPython qui permet de gérer le volume d'une mélodie pouée sur un buzzer. Le volume est contrôlé par un potentioètre.
Le but du programme est que le buzzer joue une mélodie au choix et qu'avec le potentiomètre, on puisse modifier le volume de la mélodie.

Pour avoir des notes de musique avec le buzzer, il s'uffit de trouver les fréquences correspondant au notes. Pour faire varier le volume, il s'uffit de faire varier le duty-cycle du PWM utilisé pour le buzzer.
