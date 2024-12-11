import pygame

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la ventana
screen = pygame.display.set_mode((800, 600))

# Definir el color (RGB)
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
gray = (169, 169, 169)

# Rellenar el fondo
screen.fill(white)

# Dibujar el coche

# Carrocería inferior (rectángulo)
pygame.draw.rect(screen, blue, pygame.Rect(200, 300, 400, 100))

# Carrocería superior (rectángulo)
pygame.draw.rect(screen, blue, pygame.Rect(260, 250, 280, 50))

# Ventanas (líneas que dividen la parte superior)
pygame.draw.line(screen, black, (340, 250), (340, 300), 3)
pygame.draw.line(screen, black, (420, 250), (420, 300), 3)

# Ruedas (círculos)
pygame.draw.circle(screen, black, (260, 400), 40)  # Rueda delantera
pygame.draw.circle(screen, black, (540, 400), 40)  # Rueda trasera

# Llantas (círculos más pequeños dentro de las ruedas)
pygame.draw.circle(screen, gray, (260, 400), 20)
pygame.draw.circle(screen, gray, (540, 400), 20)

# Techo (línea que conecta los puntos del techo)
pygame.draw.line(screen, black, (260, 250), (540, 250), 3)

# Actualizar la pantalla para mostrar el dibujo
pygame.display.flip()

# Mantener la ventana abierta hasta que el usuario la cierre
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Finalizar Pygame
pygame.quit()