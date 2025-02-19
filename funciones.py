import random

# Función para generar el tablero
def generar_tablero(lista:list, clave:str):
    for i in range(len(lista)):
        for j in range(1,8):
            numeros = random.randint(1,3)
            lista[i][clave].append(numeros)
    return lista

def mostrar(dic:dict, clave:str):
    for i in range(len(dic)):
        print(dic[i][clave])

# Verificar si hay 3 numeros
def verificar_vertical(lista:list, fila:int, columna:int):
    numero = lista[fila]["piezas"][columna]
    contador = 1 
    for i in range(fila - 1, -1, -1):
        if lista[i]["piezas"][columna] == numero:
            contador += 1
        else:
            break 

    for i in range(fila + 1, len(lista)):
        if lista[i]["piezas"][columna] == numero:
            contador += 1
        else:
            break  

    if contador >= 3:
        return True
    else:
        return False
        
# Guardar puntuación en archivo CSV
def guardar_puntaje(nombre:str, lista:list):
    nombre += ".csv"
    with open(nombre, "a") as archivo:
        archivo.writelines(f"{lista} \n")
    return lista

def leer_puntajes(nombre_archivo:str):
    """Lee los puntajes desde un archivo CSV y los ordena por nombre de manera ascendente."""
    jugadores = []
    nombre_archivo += ".csv"
    with open(nombre_archivo, "r") as archivo:
        for linea in archivo.readlines():
            lista = linea.strip().split(",")
            jugadores.append(lista)
    
    for i in range(len(jugadores)-1):
        for j in range(i + 1, len(jugadores)):
            if jugadores[i][0] > jugadores[j][0]:
                aux = jugadores[i]
                jugadores[i] = jugadores[j]
                jugadores[j] = aux
    return jugadores
