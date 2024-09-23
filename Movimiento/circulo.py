import pygame

# Definir Colores
VERDE = (0, 255, 0)

class Circulo():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = 0.5  # Velocidad de movimiento en pixeles

    def dibujar(self, ventana):
        pygame.draw.circle(ventana, VERDE, (self.x, self.y), 30)

    # Movimiento del circulo según las teclas presionadas
    def mover(self, teclas):
        if teclas[pygame.K_LEFT]:
            self.x -= self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.x += self.velocidad
        if teclas[pygame.K_UP]:
            self.y -= self.velocidad
        if teclas[pygame.K_DOWN]:
            self.y += self.velocidad