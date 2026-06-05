import pygame
tamaño_celda = 10
columnas = 80
filas = 60
ancho = columnas * tamaño_celda
alto = filas * tamaño_celda

Pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption("Automata de la hormiguita")

reloj = pygame.time.Clock()
FPS = 60

matriz = [[0 for _ in range(columnas)] for _ in range(filas)]
hormiga_fila = filas//2
hormiga_columna = columnas // 2

orientacion_actual = 0

def girar_hormiga(direccion):
    global orientacion_actual

    if direccion == "R":
        orientacion_actual = (orientacion_actual +1) % 4
    elif direccion == "L":
        orientacion_actual = (orientacion_actual -1) % 4 
def avanzar_hormiga():
    global hormiga_fila, hormiga_columna

    if orientacion_actual == 0:
        hormiga_fila = (hormiga_fila - 1)% filas
    elif orientacion_actual == 1:
        hormiga_columna = (hormiga_columna +1)%filas
    elif orientacion_actual == 2:
        hormiga_fila = (hormiga_fila +1) %fila
    elif orientacion_actual == 3:
        hormiga_columna = (hormiga_columna - 1) % columnas
