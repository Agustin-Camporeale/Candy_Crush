import pygame
from funciones import *
from pantalla import *

pygame.init()

# Configuración de la pantalla
ANCHO_VENTANA = 800
ALTO_VENTANA = 600
TAMAÑO_CELDA = 110 #Tamaño de las imagenes
TIEMPO_LIMITE = 10  #Duración del juego en segundos
PUNTOS_POR_ACIERTO = 10
PUNTOS_POR_FALLO = -1
TIEMPO_LIMITE = 10

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ORO = (255, 215, 0)
AZUL = (135, 206, 250)
DARKORANGE = (255, 140, 0)

# Configurar la pantalla
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Candy Crush Z") #Titulo del juego
fuente = pygame.font.Font(None, 36)

# Cargar Imágenes
logo = pygame.image.load("logo.webp")
pygame.display.set_icon(logo)
logo = pygame.transform.scale(logo, (200,200))
imagen_1 = pygame.image.load("1estrella.png")
imagen_2 = pygame.image.load("2estrella.png")
imagen_3 = pygame.image.load("3estrella.jpg")
# Redimensionar imagenes
imagen_1 = pygame.transform.scale(imagen_1, (TAMAÑO_CELDA, TAMAÑO_CELDA))
imagen_2 = pygame.transform.scale(imagen_2, (TAMAÑO_CELDA, TAMAÑO_CELDA))
imagen_3 = pygame.transform.scale(imagen_3, (TAMAÑO_CELDA, TAMAÑO_CELDA))

def iniciar_juego():
    """Funcion principal para iniciar el juego.
    Muestra la pantalla de inicio y si el jugador ingresa un nombre, empieza el juego"""
    iniciar = True
    while iniciar:
        nombre = pantalla_inicio(pantalla, fuente, logo)
        if nombre == "":
            break  # Si el usuario no ingresa un nombre, no se empieza el juego
        candy_crush(nombre, pantalla, fuente, imagen_1, imagen_2, imagen_3)

iniciar_juego()

