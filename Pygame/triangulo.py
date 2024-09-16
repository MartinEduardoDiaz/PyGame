import pygame


class Triangulo:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidad = 0.5  # Velocidad de movimiento en pixeles
        self.color = (0, 50, 255)

    def dibujar(self, ventana):
        # Vertices del triángulo
        puntos = [(self.x, self.y), (self.x - 50, self.y + 100), (self.x + 50, self.y + 100)]
        pygame.draw.polygon(ventana, self.color, puntos)

    # Movimiento del triángulo según las teclas presionadas
    def mover(self, teclas):
        if teclas[pygame.K_a]:
            self.x -= self.velocidad
        if teclas[pygame.K_d]:
            self.x += self.velocidad
        if teclas[pygame.K_w]:
            self.y -= self.velocidad
        if teclas[pygame.K_s]:
            self.y += self.velocidad