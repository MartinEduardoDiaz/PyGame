import pygame


# Triangulo

class Triangulo():
    def __init__(self, x, y, color, velocidad):
        self.x = x
        self.y = y
        self.color = color
        self.velocidad = velocidad

    def movimiento(self):
        if teclas[pygame.K_LEFT]:
            self.x = self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.y = self.velocidad

    def dibujar(self):
        triangulo = ((0,0), (0,0), (0,0))
        pygame.draw.polygon(pantalla, "red", triangulo)