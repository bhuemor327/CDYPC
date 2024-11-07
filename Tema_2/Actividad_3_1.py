import pygame
import math

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la ventana
screen = pygame.display.set_mode((800, 600))

# Definir colores que vamos a usar en formato RGB
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Rellenar el fondo
screen.fill(white)

# 1. Dibujar un punto
pygame.draw.circle(screen, black, (100, 100), 2)

# 2. Dibujar una línea
pygame.draw.line(screen, black, (150, 100), (300, 100), 5)

# 3. Dibujar un triángulo
pygame.draw.polygon(screen, green, [(400, 100), (350, 150), (450, 150)])

# 4. Dibujar un cuadrado (usando un rectángulo)
pygame.draw.rect(screen, blue, pygame.Rect(500, 100, 50, 50))

# 5. Dibujar un rectángulo
pygame.draw.rect(screen, red, pygame.Rect(600, 100, 100, 50))

# 6. Dibujar un círculo
pygame.draw.circle(screen, black, (150, 300), 50)

# 7. Dibujar una elipse
pygame.draw.ellipse(screen, green, pygame.Rect(250, 250, 150, 80))

# 8. Dibujar un arco (sector de un círculo)
pygame.draw.arc(screen, red, pygame.Rect(450, 250, 150, 80), 0, math.pi/2, 5)

# 9. Dibujar un sector de un círculo (usando una superficie y polígonos)
pygame.draw.polygon(screen, blue, [(600, 300), (650, 300), (620, 250)])

# Actualizar la pantalla para mostrar los dibujos
pygame.display.flip()

# Mantener la ventana abierta hasta que el usuario la cierre
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Finalizar Pygame
pygame.quit()