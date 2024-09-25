# Inicializar Pygame
import pygame
pygame.init()

# Crear Ventana
tamaño = (800,500)
ventana = pygame.display.set_mode(tamaño)

# Bucle para que la Ventana se mantenga
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False