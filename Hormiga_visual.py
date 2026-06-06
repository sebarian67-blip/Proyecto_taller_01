import pygame
import random
import sys
import Hormiga_logica as hor
import colorsys
tam = 3
filas = 200
columnas = 200
tick = 0

def generar_colores(cantidad_colores):
    """Funcion encargada de generar los colores que
    la hormiga usa para "pintar":
    Entradas: Recibe como parametro:
        - cantidad_colores
    Restricciones: no tiene, evaluadas en el main
    Salidas:
        - colores"""
    colores = [(25, 40, 30)]  
    
    if cantidad_colores <= 1:
        return colores
    pasos = cantidad_colores - 1
    for i in range(pasos):
        colosh = i / pasos
        r, g, b = colorsys.hsv_to_rgb(colosh, 1.0, 1.0)
        
        colores.append((int(r * 255), int(g * 255), int(b * 255)))
        
    return colores


def main():
    """Funcion principal de el programa encargada de recibir y llamar a las demás funciones:
    Entradas:
        - regla
    Restricciones: regla debe de ser una combinacion de Ls o Rs.
    Salidas:
        - Generacion de la hormiga"""
    regla = input("Ingrese la secuencia de giros: ").strip().upper()
    while not regla or any(letra not in "LR" for letra in regla):
        print("Error: La regla solo puede contener letras 'L' y 'R'.")
        regla = input("Intente de nuevo: ").strip().upper()

    paleta_colores = generar_colores(len(regla))
    
    filaHormiga = filas // 2
    columnaHormiga = columnas // 2
    direccion = "R"
    
    pygame.init()
    clock = pygame.time.Clock()
    M = hor.generar_matriz(filas, columnas)
    w, h = columnas * tam, filas * tam
    window = pygame.display.set_mode((w, h))
    pygame.display.set_caption("Hormiga de Langton Proyecto")
    
    loop = True
    pausa = False
    
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    pausa = not pausa
            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons = pygame.mouse.get_pressed()
                x, y = pygame.mouse.get_pos()
                if buttons[0]:
                    f = y // tam
                    c = x // tam
                    M[f][c] = (M[f][c] + 1) % len(regla)
                    
        window.fill(paleta_colores[0])
        
        for f in range(filas):
            for c in range(columnas):
                color_estado = M[f][c]
                color_rgb = paleta_colores[color_estado]
                
                if color_estado != 0:
                    pos_x = c * tam
                    pos_y = f * tam
                    pygame.draw.rect(window, color_rgb, (pos_x, pos_y, tam, tam))
        x_hormiga = columnaHormiga * tam
        y_hormiga = filaHormiga * tam
        pygame.draw.rect(window, (255, 0, 0), (x_hormiga, y_hormiga, tam, tam))
                    
        if not pausa:
            M, filaHormiga, columnaHormiga, direccion = hor.siguiente(M, filaHormiga, columnaHormiga, direccion, regla)
            
        pygame.display.update()
        clock.tick(tick)
        
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
