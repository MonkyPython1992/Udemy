import pygame
import random

# Inicializar Pygame
pygame.init()

# Crear una ventana para mostrar las imágenes
ventana = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Juego del Ahorcado")

# Cargar las imágenes
imagenes = []
for i in range(7):
    imagen = pygame.image.load("imagen" + str(i) + ".jpg")
    imagenes.append(imagen)

# Lista de palabras
palabras = ["perro", "gato", "raton", "elefante", "hipopotamo"]

# Elije una palabra al azar
palabra = random.choice(palabras)

# Convierte la palabra en una lista de letras
letras = list(palabra)

# Crea una lista de letras adivinadas
letras_adivinadas = []

# Crea una variable para contar el número de intentos
intentos = 0

# Bucle principal del juego
while True:
    # Imprime la palabra con las letras adivinadas
    imprimir = ""
    for letra in letras:
        if letra in letras_adivinadas:
            imprimir += letra
        else:
            imprimir += "_"
    print(imprimir)

    # Mostrar la imagen correspondiente al número de intentos
    ventana.blit(imagenes[intentos], (0, 0))
    pygame.display.update()

    # Pide una letra al usuario
    letra = input("Adivina una letra: ")

    # Aumenta el número de intentos
    intentos += 1

    # Comprueba si la letra está en la palabra
    if letra in letras:
        letras_adivinadas.append(letra)
    else:
        print("La letra no está en la palabra.")

    # Comprueba si el usuario ha adivinado todas las letras
    if set(letras) == set(letras_adivinadas):
        print("¡Felicidades! Adivinaste la palabra en", intentos, "intentos.")
        break
    elif intentos >= 6:
        print("Perdiste, la palabra era", palabra)
        break
