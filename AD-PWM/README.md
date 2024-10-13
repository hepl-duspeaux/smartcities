# Exercice 2: volume d'une mélodie

Créer un programme MicroPython qui permet de gérer le volume d'une mélodie jouée sur un buzzer. Le volume est contrôlé par un potentioètre.
Le but du programme est que le buzzer joue une mélodie au choix et qu'avec le potentiomètre, on puisse modifier le volume de la mélodie.

Pour avoir des notes de musique avec le buzzer, il s'uffit de trouver les fréquences correspondant au notes. Pour faire varier le volume, il s'uffit de faire varier le duty-cycle du PWM utilisé pour le buzzer.

## Organigramme

![{804AEF16-810B-4DAF-AC4A-C603918C3EE8}](https://github.com/user-attachments/assets/fd789aec-7b00-4edc-97fb-c3d55d132d75)

Dans le code, on retrouve l'initialisation des GPIO et de l'interruption du timer. Ensuite les fonctions qui me permettent de manipuler les notes de musique plutot que les fréquences. Dans la boucle principale, il ne reste plus qu'à appeller les notes et les séparer par les delay.
L'interruption lit la valeur analogique du potentiomètre à une fréquence de 100Hz.
