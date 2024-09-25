import pygame

AZUL = (0, 0, 255)

class Circulo():
    def __init__(self, x, y, teclapresionada):
        self.x = x
        self.y = y
        self.velocidad = 0.5
        self.teclapresionada = teclapresionada
    
    def dibujar(self, ventana):
        pygame.draw.circle(ventana, AZUL, (self.x, self.y), 60)
    
    def mover(self, teclas):
        if teclas[self.teclapresionada['tecla_izquierda']]:
            self.x -= self.velocidad
        if teclas[self.teclapresionada['tecla_derecha']]:
            self.x += self.velocidad
        if teclas[self.teclapresionada['tecla_arriba']]:
            self.y -= self.velocidad
        if teclas[self.teclapresionada['tecla_abajo']]:
            self.y += self.velocidad

circulo1 = {
    'tecla_izquierda': pygame.K_a,
    'tecla_derecha': pygame.K_d,
    'tecla_arriba': pygame.K_w,
    'tecla_abajo': pygame.K_s,
}