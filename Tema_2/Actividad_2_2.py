import pygame

# Inicializar Pygame
pygame.init()

# Definir el tamaño de la ventana
screen = pygame.display.set_mode((800, 600))

# Definir los colores (RGB)
water_blue = (0, 191, 255)  # Fondo de agua
fish_body_color = (255, 165, 0)  # Color del cuerpo del pez (naranja)
fish_tail_color = (255, 69, 0)  # Color de la cola (rojo)
fish_fin_color = (255, 215, 0)  # Color de las aletas (amarillo)
eye_color = (0, 0, 0)  # Color de los ojos (negro)

# Rellenar el fondo con color agua
screen.fill(water_blue)

# Dibujar el pez

# Cuerpo del pez (elipse)
pygame.draw.ellipse(screen, fish_body_color, pygame.Rect(300, 250, 200, 100))

# Cola del pez (triángulo)
pygame.draw.polygon(screen, fish_body_color, [(450, 300), (600, 250), (600, 350)])

# Aletas del pez (formas triangulares)
pygame.draw.polygon(screen, fish_fin_color, [(450, 270), (450, 240), (430, 270)])  # Aleta superior
pygame.draw.polygon(screen, fish_fin_color, [(450, 330), (450, 360), (430, 330)])  # Aleta inferior

# Ojo del pez (círculo)
pygame.draw.circle(screen, eye_color, (350, 280), 10)

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
