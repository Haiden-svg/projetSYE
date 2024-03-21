import turtle

class Graphics:
    def __init__(self, longueur):
        self.longueur = longueur

    def dessiner(self):
        turtle.forward(self.longueur)
        turtle.right(90)
        turtle.forward(self.longueur)
        turtle.right(90)
        turtle.forward(self.longueur)
        turtle.right(90)
        turtle.forward(self.longueur)
        turtle.right(90)

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