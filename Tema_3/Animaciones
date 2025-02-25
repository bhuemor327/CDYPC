import pygame
import sys

# Inicializamos Pygame
pygame.init()

# Definimos el tamaño de la ventana
ancho_ventana = 800
alto_ventana = 600
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption('Animación básica')

# Definimos colores
blanco = (255, 255, 255)
azul = (0, 128, 255)

# Posición inicial del círculo
x = 0
y = alto_ventana // 2
radio = 30

# Velocidad de movimiento
velocidad_x = 5

# Reloj para controlar los FPS
reloj = pygame.time.Clock()

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Actualizamos la posición del círculo
    x += velocidad_x
    if x > ancho_ventana + radio:
        x = -radio  # Reiniciamos la posición

    # Rellenamos el fondo
    ventana.fill(blanco)

    # Dibujamos el círculo
    pygame.draw.circle(ventana, azul, (x, y), radio)

    # Actualizamos la pantalla
    pygame.display.flip()

    # Controlamos los FPS
    reloj.tick(60)  # 60 FPS
