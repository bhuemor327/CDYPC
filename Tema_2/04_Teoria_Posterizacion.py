from PIL import Image

# Abrimos la imagen original
imagen_original = Image.open('Gato.jpg')

# Aseguramos que la imagen esté en modo RGB
imagen_rgb = imagen_original.convert('RGB')

# Establecemos el número de niveles de posterización
niveles = 4  # Puedes cambiar este número para experimentar

# Calculamos el tamaño de cada nivel
tamaño_nivel = 256 // niveles

# Creamos una nueva imagen vacía con el mismo tamaño
imagen_posterizada = Image.new('RGB', imagen_rgb.size)

# Obtenemos las dimensiones de la imagen
ancho, alto = imagen_rgb.size

# Recorremos cada píxel de la imagen
for x in range(ancho):
    for y in range(alto):
        # Obtenemos el color del píxel actual
        r, g, b = imagen_rgb.getpixel((x, y))

        # Calculamos el nuevo valor de cada componente
        r_nuevo = int(r / tamaño_nivel) * tamaño_nivel
        g_nuevo = int(g / tamaño_nivel) * tamaño_nivel
        b_nuevo = int(b / tamaño_nivel) * tamaño_nivel

        # Aseguramos que los valores no excedan 255
        r_nuevo = min(r_nuevo, 255)
        g_nuevo = min(g_nuevo, 255)
        b_nuevo = min(b_nuevo, 255)

        # Asignamos el nuevo color al píxel de la nueva imagen
        imagen_posterizada.putpixel((x, y), (r_nuevo, g_nuevo, b_nuevo))

# Guardamos la imagen posterizada
imagen_posterizada.save('Gato_posterizado.jpg')