# Importamos dos librerias: pygame para crear aplicaciones gráficas y math para utilizar funciones matemáticas
import pygame
import math

# Inicializar Pygame para que todo funcione
pygame.init()

# Definir el tamaño de la ventana: 800 pixeles de ancho y 600 de alto
screen = pygame.display.set_mode((800, 600))

# Definir colores que vamos a usar en formato RGB (rojo, verde, azul), donde cada componente tiene valores
# entre 0 y 255. Por ejemplo, (255, 0, 0) es rojo, (0, 0, 255) es azul, y así sucesivamente.
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Rellenar el fondo de la ventana en color blanco
screen.fill(white)

# 1. Dibujar un punto de color negro, en la posición 100x100 y de radio 2
pygame.draw.circle(screen, black, (100, 100), 2)

# 2. Dibujar una línea de color negro que empieza en la posición 150x100 y acaba en la posición 300x100
# con un grosor de 5 píxeles
pygame.draw.line(screen, black, (150, 100), (300, 100), 5)

# 3. Dibujar un triángulo indicando los vértices
pygame.draw.polygon(screen, green, [(400, 100), (350, 150), (450, 150)])

# 4. Dibujar un cuadrado (usando un rectángulo) en la posición 500x100 de medidas 50x50
pygame.draw.rect(screen, blue, pygame.Rect(500, 100, 50, 50))

# 5. Dibujar un rectángulo en la posición 600x100 de medidas 100x50
pygame.draw.rect(screen, red, pygame.Rect(600, 100, 100, 50))

# 6. Dibujar un círculo indicando el centro y radio
pygame.draw.circle(screen, black, (150, 300), 50)

# 7. Dibujar una elipse dentro de un rectángulo delimitador
pygame.draw.ellipse(screen, green, pygame.Rect(250, 250, 150, 80))

# 8. Dibujar un arco (sector de un círculo)
# Dibuja un arco en rojo dentro de un rectángulo de tamaño 150x80 píxeles.
# El arco empieza en el ángulo 0 (0 radianes) y termina en π/2 (90 grados), con un grosor de línea de 5 píxele
pygame.draw.arc(screen, red, pygame.Rect(450, 250, 150, 80), 0, math.pi/2, 5)

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