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
    
