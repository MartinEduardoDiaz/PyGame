import pygame

# Definir Colores
BLANCO = (255, 255, 255)

class Cuadrado:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = 0.5  # Velocidad de movimiento en pixeles
        self.color = BLANCO

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, BLANCO, (self.x, self.y, 60, 60))

    # Movimiento del cuadrado según las teclas presionadas
    def mover(self, teclas):
        if teclas[pygame.K_j]:
            self.x -= self.velocidad
        if teclas[pygame.K_l]:
            self.x += self.velocidad
        if teclas[pygame.K_i]:
            self.y -= self.velocidad
        if teclas[pygame.K_k]:
            self.y += self.velocidad