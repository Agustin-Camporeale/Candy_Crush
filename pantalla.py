import pygame
from funciones import *

ANCHO_VENTANA = 800
ALTO_VENTANA = 600
TAMAÑO_CELDA = 110
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ORO = (255, 215, 0)
AZUL = (135, 206, 250)
DARKORANGE = (255, 140, 0)

def dibujar_tablero(tablero, pantalla, img1, img2, img3):
    filas = len(tablero)
    columnas = 7
    for fila in range(filas):
        for columna in range(columnas):
            x = columna * 110
            y = fila * 110
            if tablero[fila]["piezas"][columna] == 1:
                pantalla.blit(img1, (x + 20, y + 150))
            elif tablero[fila]["piezas"][columna] == 2:
                pantalla.blit(img2, (x + 20, y + 150))
            elif tablero[fila]["piezas"][columna] == 3:
                pantalla.blit(img3, (x + 20, y + 150))
    return tablero

def pantalla_inicio(pantalla, fuente, logo):
    reloj = pygame.time.Clock()
    entrada_nombre = ""
    activo = False

    boton_jugar = pygame.Rect(300, 450, 200, 50)  
    boton_scoreboard = pygame.Rect(300, 520, 200, 50)
    input_nombre = pygame.Rect(300, 350, 200, 50)  

    while True:
        pantalla.fill(ORO)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return None
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if input_nombre.collidepoint(evento.pos):
                    activo = True  # Activar escritura en el cuadro de texto
                if boton_jugar.collidepoint(evento.pos) and entrada_nombre:
                    print(f"Nombre: {entrada_nombre}")  
                    return entrada_nombre  # Iniciar el juego con el nombre ingresado
                if boton_scoreboard.collidepoint(evento.pos):
                    mostrar_scoreboard(pantalla, fuente)

            elif evento.type == pygame.KEYDOWN and activo:
                if evento.key == pygame.K_BACKSPACE:
                    entrada_nombre = entrada_nombre[:-1]
                elif len(entrada_nombre) < 12:  # Maximo de 12 caracteres al nombre
                    entrada_nombre += evento.unicode

        # Dibujar elementos de la pantalla
        titulo = fuente.render("CANDY CRUSH Z", True, NEGRO)
        pantalla.blit(titulo, (300, 50))
        pantalla.blit(logo, (300, 100))

        # Dibujar el cuadro de texto
        pygame.draw.rect(pantalla, DARKORANGE, input_nombre)
        texto_input = fuente.render(entrada_nombre, True, NEGRO)
        pantalla.blit(texto_input, (310, 360)) 

        # Dibujar botones
        pygame.draw.rect(pantalla, DARKORANGE, boton_jugar)
        pygame.draw.rect(pantalla, DARKORANGE, boton_scoreboard)
        texto_jugar = fuente.render("JUGAR", True, NEGRO)
        texto_scoreboard = fuente.render("SCOREBOARD", True, NEGRO)
        pantalla.blit(texto_jugar, (355, 460))
        pantalla.blit(texto_scoreboard, (315, 535))

        pygame.display.flip()
        reloj.tick(30)

# Mostrar el scoreboard
def mostrar_scoreboard(pantalla, fuente):
    score = leer_puntajes("Scoreboard")
    reloj = pygame.time.Clock()
    while True:
        pantalla.fill(ORO)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    return  # Volver a la pantalla de inicio

        titulo = fuente.render("SCOREBOARD", True, NEGRO)
        pantalla.blit(titulo, (310, 40))
        y_textos = 120
        for elemento in score:  
            texto = fuente.render(f"{elemento[0]},{elemento[1]}", True, NEGRO)
            pantalla.blit(texto, (320, y_textos))
            y_textos += 40

        pygame.display.flip()
        reloj.tick(30)

def candy_crush(nombre, pantalla, fuente, imagen_1, imagen_2, imagen_3):
    logo = pygame.image.load("logo.webp")
    pygame.display.set_icon(logo)
    logo = pygame.transform.scale(logo, (200,125))
    lista = [
    {"piezas":[]},
    {"piezas":[]},
    {"piezas":[]},
    {"piezas":[]}
    ]

    tablero = generar_tablero(lista, "piezas")
    reloj = pygame.time.Clock()
    tiempo_restante = 10
    puntos = 0
    sonido_acierto = pygame.mixer.Sound("acierto.mp3")
    sonido_error = pygame.mixer.Sound("error.mp3")
    volumen = 0.05
    sonido_acierto.set_volume(volumen)
    sonido_error.set_volume(volumen)
    TIMER_EVENTO = pygame.USEREVENT + 1
    pygame.time.set_timer(TIMER_EVENTO, 1000)
    
    while tiempo_restante > 0:
        pantalla.fill(ORO)
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                return
            elif evento.type == TIMER_EVENTO:  # Evento que reduce el tiempo
                tiempo_restante -= 1
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                x, y = evento.pos
                print(x,y)
                columna = (x - 40) // TAMAÑO_CELDA
                fila = (y - 135) // TAMAÑO_CELDA
                print(fila,columna)

                if 0 <= fila < 4 and 0 <= columna < 7:
                    if verificar_vertical(tablero, fila, columna):
                        puntos += 10
                        sonido_acierto.play()
                        lista = [
                            {"piezas":[]},
                            {"piezas":[]},
                            {"piezas":[]},
                            {"piezas":[]}
                        ]   
                        tablero = generar_tablero(lista, "piezas")
                    else:
                        puntos -= 1
                        tiempo_restante -= 1
                        sonido_error.play()
                        lista = [
                            {"piezas":[]},
                            {"piezas":[]},
                            {"piezas":[]},
                            {"piezas":[]}
                        ]   
                        tablero = generar_tablero(lista, "piezas")

        # Dibujar elementos
        dibujar_tablero(tablero, pantalla, imagen_1, imagen_2, imagen_3)
        texto_puntos = fuente.render(f"Puntos: {puntos}", True, NEGRO)
        texto_tiempo = fuente.render(f"Tiempo: {tiempo_restante}s", True, NEGRO)
        pantalla.blit(texto_puntos, (10, 10))
        pantalla.blit(texto_tiempo, (10, 50))
        pantalla.blit(logo, (300, 10))
        pygame.display.flip()
        reloj.tick(30)
    jugadores = [nombre,puntos]
    guardar_puntaje("Scoreboard", jugadores)
