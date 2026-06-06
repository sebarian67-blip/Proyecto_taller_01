import pygame
import logicaVida as con
import pickle
import easygui

tick = 10

def pedir_parametros():
    """
    Propósito: ingresar los parámetros iniciales.
    Entradas:
        None
    Restricciones:
        None
    Salidas:
        b: str (dígitos del '0' al '8').
        s: str (dígitos del '0' al '8').
        filas: int (positivo, de 1 a 10000).
        columnas: int (positivo, de 1 a 10000).
        tam: int (positivo, de 1 a 50)."""
    b = easygui.enterbox("Ingrese String B (nacimiento, ej: 3):", "Reglas B")
    s = easygui.enterbox("Ingrese String S (supervivencia, ej: 23):", "Reglas S")
    filas = easygui.integerbox("Cantidad de filas:", "Dimensiones", default=200, lowerbound=1, upperbound=10000)
    columnas = easygui.integerbox("Cantidad de columnas:", "Dimensiones", default=200, lowerbound=1, upperbound=10000)
    tam = easygui.integerbox("Tamaño de celda (px):", "Tamaño", default=10, lowerbound=1, upperbound=50)
    return b, s, filas, columnas, tam

def main():
    """
    Propósito: ejecutar el bucle principal del autómata celular controlando la interfaz gráfica y los eventos.
    Entradas:
        Ninguna directa (obtiene b, s, filas, columnas, tam desde la función pedir_parametros).
    Restricciones:
        None
    Salidas:
        None"""
    b,s,filas,columnas,tam = pedir_parametros()
    if not s.isdigit() or not b.isdigit() or "9" in s or "9" in b:
        raise Exception("ERROR!! ESO NO SE HACE, B y S deben contener solo números del 0 al 8.")
    if type(filas) != int or type(columnas) != int or type(tam) != int or filas<0 or columnas<0 or tam<0:
        raise Exception("ERROR!! ESO NO SE HACE, para la cantidad de filas, columna y tamaño use números enteros positivos.")
    
    pygame.init()
    clock = pygame.time.Clock()
    M = con.generar_matriz_aleatoria(filas, columnas)
    w, h = columnas * tam, filas * tam
    window = pygame.display.set_mode((w, h))
    loop = True
    pausa = False

    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pausa = not pausa
                if event.key == pygame.K_g:
                    estado = {
                        'filas': filas,
                        'columnas': columnas,
                        'tam': tam,
                        'b': b,
                        's': s,
                        'matriz': M
                    }
                    try:
                        with open('automata_save.pkl', 'wb') as f:
                            pickle.dump(estado, f)
                        print("Estado guardado en 'automata_save.pkl'")
                    except Exception as e:
                        print(f"Error al guardar: {e}")
                if event.key == pygame.K_c:
                    try:
                        with open('automata_save.pkl', 'rb') as f:
                            estado = pickle.load(f)
                        filas = estado['filas']
                        columnas = estado['columnas']
                        tam = estado['tam']
                        b = estado['b']
                        s = estado['s']
                        M = estado['matriz']
                        nueva_w = columnas * tam
                        nueva_h = filas * tam
                        if (nueva_w, nueva_h) != window.get_size():
                            window = pygame.display.set_mode((nueva_w, nueva_h))
                            print(f"Ventana redimensionada a {nueva_w}x{nueva_h}")
                        print("Estado cargado correctamente desde 'automata_save.pkl'")
                        print(f"B={b}, S={s}, Filas={filas}, Columnas={columnas}, Tamaño celda={tam}")
                    except FileNotFoundError:
                        print("Archivo 'automata_save.pkl' no encontrado. Primero guarda con la tecla G.")
                    except Exception as e:
                        print(f"Error al cargar: {e}")
                if event.key == pygame.K_r:
                    M = con.generar_matriz_aleatoria(filas, columnas)
                    print("Matriz reiniciada con valores aleatorios (R)")
                if event.key == pygame.K_b:
                    M = con.generar_matriz_vacia(filas, columnas)
                    print("Matriz reiniciada con valores neutros (B)")

            if event.type == pygame.MOUSEBUTTONDOWN:
                buttons = pygame.mouse.get_pressed()
                x, y = pygame.mouse.get_pos()
                if buttons[0]:
                    f = y // tam
                    c = x // tam
                    if 0 <= f < filas and 0 <= c < columnas:
                        M[f][c] = (M[f][c] + 1) % 2

        window.fill((0, 0, 0))
        for f in range(filas):
            for c in range(columnas):
                if M[f][c] == 1:
                    x = c * tam
                    y = f * tam
                    pygame.draw.rect(window, (0, 255, 128), (x, y, tam, tam))
        if not pausa:
            M = con.transicion(M, b, s)
        pygame.display.update()
        clock.tick(tick)
    pygame.quit()

if __name__ == "__main__":
    main()
