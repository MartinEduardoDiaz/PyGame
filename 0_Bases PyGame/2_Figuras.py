# Inicializar Pygame
import pygame
pygame.init()

# Definir Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0 , 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

tamaño = (800,500)
ventana = pygame.display.set_mode(tamaño)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Color de Fondo
    ventana.fill(BLANCO)

    # --- Dibujo
    pygame.draw.line(ventana, ROJO, [0, 100], [100, 100], 5)
    pygame.draw.rect(ventana, AZUL, (100, 100, 80, 80))
    pygame.draw.circle(ventana, VERDE, (200, 200), 30)
    # --- Fin Dibujo

    # Actualizar Pantalla
    pygame.display.flip()