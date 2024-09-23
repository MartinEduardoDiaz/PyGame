import pygame
from circulo import Circulo

pygame.init()

ventana = pygame.display.set_mode((800, 600)) 
pygame.display.set_caption("Movimiento de Circulo")

background_color = (0, 0, 0)

# Instancia de la clase Triangulo
# Posición inicial del Triangulo en el plano
circulo = Circulo(400, 100)  

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Estado de las teclas
    teclas = pygame.key.get_pressed()

    # Mover el triángulo
    circulo.mover(teclas)

    # Pintar el fondo
    ventana.fill(background_color)

    # Dibujar el triángulo
    circulo.dibujar(ventana)

    # Actualizar la pantalla
    pygame.display.update()

# Cerrar Pygame
pygame.quit()