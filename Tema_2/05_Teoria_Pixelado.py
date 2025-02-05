from PIL import Image

# Abrimos la imagen original
imagen_original = Image.open('Gato.jpg')

# Definimos el tamaño de los píxeles grandes
tamano_pixel = 10  # Puedes cambiar este valor para ver diferentes efectos

# Obtenemos las dimensiones de la imagen
ancho, alto = imagen_original.size

# Redimensionamos la imagen a un tamaño más pequeño
imagen_pequena = imagen_original.resize(
    (ancho // tamano_pixel, alto // tamano_pixel),
    resample=Image.NEAREST)

# Volvemos a ampliar la imagen al tamaño original
imagen_pixelada = imagen_pequena.resize(
    (ancho, alto),
    resample=Image.NEAREST)

# Guardamos la imagen pixelada
imagen_pixelada.save('Gato_pixelada.jpg')
