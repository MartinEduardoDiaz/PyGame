import pygame

AZUL = (0, 0, 255)

class Circulo():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = 0.5
    
    def dibujar(self, ventana):
        pygame.draw.circle(ventana, AZUL, (self.x, self.y), 60)
    
    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.x += self.velocidad
        if teclas[pygame.K_UP]:
            self.y -= self.velocidad
        if teclas[pygame.K_DOWN]:
            self.y += self.velocidad