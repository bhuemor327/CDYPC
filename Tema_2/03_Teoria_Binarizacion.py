from PIL import Image

# Abrimos la imagen original
imagen_original = Image.open('Gato.jpg')

# Convertimos la imagen a escala de grises
imagen_gris = imagen_original.convert('L')

# Creamos una nueva imagen vacía con el mismo tamaño
imagen_binarizada = Image.new('L', imagen_gris.size)

# Establecemos el umbral para la binarización
umbral = 128

# Obtenemos las dimensiones de la imagen
ancho, alto = imagen_gris.size

# Aplicamos la binarización
for x in range(ancho):
    for y in range(alto):
        # Obtenemos el valor de luminosidad del píxel actual
        valor = imagen_gris.getpixel((x, y))

        # Si el valor es mayor que el umbral, lo establecemos en blanco (255)
        # Si es menor o igual, lo establecemos en negro (0)
        if valor > umbral:
            imagen_binarizada.putpixel((x, y), 255)
        else:
            imagen_binarizada.putpixel((x, y), 0)

# Guardamos la imagen binarizada
imagen_binarizada.save('Gato_binarizada.png')