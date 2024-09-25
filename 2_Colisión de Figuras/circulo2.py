import pygame

VERDE = (0, 187, 51)

class Circulo2():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = 0.5
    
    def dibujar(self, ventana):
        pygame.draw.circle(ventana, VERDE, (self.x, self.y), 60)
    
    def mover(self, teclas):
        if teclas[pygame.K_a]:
            self.x -= self.velocidad
        if teclas[pygame.K_d]:
            self.x += self.velocidad
        if teclas[pygame.K_w]:
            self.y -= self.velocidad
        if teclas[pygame.K_s]:
            self.y += self.velocidad