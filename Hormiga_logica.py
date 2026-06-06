def generar_matriz(filas, columnas):
    """Funcion de la logica, encargada de la generacion de una matriz con 0s:
    Entradas: recibe como parametros:
        - filas
        - columnas.
    Restricciones: no tiene.
    Salida: La matriz de 0s."""

    return [[0 for c in range (columnas)] for f in range(filas)]

def girar_hormiga(orientacion_actual, giro):
    """Funcion de la logica encargada de la direccion que la hormiga toma segun su posicion actual:
    Entradas: recibe como parametros a:
        - orientacion_actual
        - giro
     Restricciones: no tiene
     Salidas:
        - giro_derecha
        - giro_izquierda"""
    giro_derecha = {"U": "R", "R": "D", "D": "L", "L": "U"}
    giro_izquierda = {"U": "L", "L": "D", "D": "R", "R": "U"}
    
    if giro == "R":
        return giro_derecha[orientacion_actual]
    else:
        return giro_izquierda[orientacion_actual]
        
def avanzar_hormiga(filaHormiga, columnaHormiga, direccion, total_filas, total_columnas):
    """Funcion de logica que se encarga de el avance de la hormiga según su posición actual:
    Entradas: recibe como parametros:
        - filaHormiga
        - columnaHormiga
        - direccion
        - total_filas
        - total_columnas
    Restricciones: no tiene
    Salidas: avanzar_hormiga"""
    if direccion == "R":
        return filaHormiga, (columnaHormiga + 1) % total_columnas
    if direccion == "L":
        return filaHormiga, (columnaHormiga - 1) % total_columnas
    if direccion == "U":
        return (filaHormiga - 1) % total_filas, columnaHormiga
    if direccion == "D":
        return (filaHormiga + 1) % total_filas, columnaHormiga

def transicion(M, filaHormiga, columnaHormiga, regla):
    """Subfunción de siguiente() que se encarga de actualizar
    la matriz para generar el camino de la hormiga.
    Entradas: recibe como parametros:
        - M
        - filaHormiga
        - columnaHormiga
        - regla
    Restricciones: no tiene
    Salidas: M """
    total_colores = len(regla)
    color_actual = M[filaHormiga][columnaHormiga]
    siguiente_color = (color_actual + 1) % total_colores
    M[filaHormiga][columnaHormiga] = siguiente_color
    return M
def siguiente(M, filaHormiga, columnaHormiga, direccion, regla):
    """Funcion que se encarga de analizar el color actual y llamar a transicion() para actualizar la matriz.
    Entradas: recibe como parametros a:
        - M
        - filaHormiga
        - columnaHormiga
        - direccion
        - regla
    Restricciones: no tiene
    Salidas:
        - M
        - filaHormiga
        -columnaHormiga
        -direccion """
    color_actual = M[filaHormiga][columnaHormiga]
    giro = regla[color_actual]
    direccion = girar_hormiga(direccion, giro)
    M = transicion(M, filaHormiga, columnaHormiga, regla)
    total_filas = len(M)
    total_columnas = len(M[0])
    filaHormiga, columnaHormiga = avanzar_hormiga(filaHormiga, columnaHormiga, direccion, total_filas, total_columnas)
    
    return M, filaHormiga, columnaHormiga, direccion
