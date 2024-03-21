import turtle
class Main:
    def __init__(self):
        turtle.speed(0)  # Set the turtle speed to the fastest
        self.c = Graphics(100)

    def dessiner_carre(self):
        self.c.dessiner()

# Exemple d'utilisation
m = Main()
m.dessiner_carre()

turtle.done()