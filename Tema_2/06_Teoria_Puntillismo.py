from PIL import Image, ImageDraw
import random

# Abrimos la imagen original
imagen_original = Image.open('Gato.jpg')

# Convertimos la imagen a modo RGB
imagen_rgb = imagen_original.convert('RGB')

# Definimos el tamaño de los puntos
tamano_punto = 5  # Puedes cambiar este valor para ver diferentes efectos

# Obtenemos las dimensiones de la imagen
ancho, alto = imagen_rgb.size

# Número de cuadros para la animación
numero_cuadros = 10  # Puedes aumentar este número para una animación más larga

# Lista para almacenar los cuadros de la animación
cuadros = []

for i in range(numero_cuadros):
    # Creamos una nueva imagen en blanco
    imagen_puntillismo = Image.new('RGB', (ancho, alto), color='white')
    draw = ImageDraw.Draw(imagen_puntillismo)

    # Recorremos la imagen en pasos del tamaño de los puntos
    for x in range(0, ancho, tamano_punto):
        for y in range(0, alto, tamano_punto):
            # Obtenemos el color del píxel actual
            r, g, b = imagen_rgb.getpixel((x, y))

            # Añadimos una variación aleatoria al color para el efecto animado
            variacion = random.randint(-20, 20)
            r_nuevo = min(max(r + variacion, 0), 255)
            g_nuevo = min(max(g + variacion, 0), 255)
            b_nuevo = min(max(b + variacion, 0), 255)

            # Dibujamos un punto (círculo) en la posición actual
            draw.ellipse(
                (x, y, x + tamano_punto, y + tamano_punto),
                fill=(int(r_nuevo), int(g_nuevo), int(b_nuevo))
            )

    # Añadimos el cuadro actual a la lista de cuadros
    cuadros.append(imagen_puntillismo)

# Guardamos los cuadros como una animación GIF
cuadros[0].save(
    'Gato_animado.gif',
    save_all=True,
    append_images=cuadros[1:],
    duration=200,
    loop=0
)