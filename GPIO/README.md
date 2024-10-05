# Exercice 1: clignotement de LED avec bouton poussoir

Créer un programme MicroPython qui permet de clignoter une LED à différentes vitesses en fonction du nombre de pression sur un bouton poussoir.

Lorsque l'on presse le bouton une fois la LED doit clignoter à une fréquence de 0.5Hz. Lorsque l'on appuie une deuxième fois, la LED doit clignotée plus vite et elle doit s'éteindre si on appuie une troisième fois.

## Organigramme

![{FE08DFDE-96F2-4CC2-9F89-5B3CC8A753C5}](https://github.com/user-attachments/assets/4481294e-ae53-4ef1-8788-7d020523ba0d)

Le code que j'ai fait regarde la valeur de value et en foncion de celle-ci fait clignoter plus ou moins vite la LED. La valeur de value est changée lorsque 'on appuie sur le bouton poussoir via une interruption.
