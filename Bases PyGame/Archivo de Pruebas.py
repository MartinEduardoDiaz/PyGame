import pygame
pygame.init()

ventana = pygame.display.set_mode([800, 600])

# Nombre de Ventana
pygame.display.set_caption("Pruebas")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

