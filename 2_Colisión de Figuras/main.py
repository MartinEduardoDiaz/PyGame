import pygame

from circulo import Circulo
from circulo2 import Circulo2

pygame.init()


BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)


circulo = Circulo(400, 100)
circulo2 = Circulo2(400, 100)

ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Colisiones")

##
##

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    teclas = pygame.key.get_pressed()
    circulo.mover(teclas)
    circulo2.mover(teclas)

    ventana.fill(BLANCO)

    circulo.dibujar(ventana)
    circulo2.dibujar(ventana)

    pygame.display.update()