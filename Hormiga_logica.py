def generar_matriz(filas, columnas):
    """ matriz puros 0s"""

    return [[0 for c in range (columnas)] for f in range(filas)]

def girar_hormiga(orientacion_actual, giro):
    
    giro_derecha = {"U": "R", "R": "D", "D": "L", "L": "U"}
    giro_izquierda = {"U": "L", "L": "D", "D": "R", "R": "U"}
    
    if giro == "R":
        return giro_derecha[orientacion_actual]
    else:
        return giro_izquierda[orientacion_actual]
        
def avanzar_hormiga(filaHormiga, columnaHormiga, direccion, total_filas, total_columnas):
    
    if direccion == "R":
        return filaHormiga, (columnaHormiga + 1) % total_columnas
    if direccion == "L":
        return filaHormiga, (columnaHormiga - 1) % total_columnas
    if direccion == "U":
        return (filaHormiga - 1) % total_filas, columnaHormiga
    if direccion == "D":
        return (filaHormiga + 1) % total_filas, columnaHormiga

def transicion(M, filaHormiga, columnaHormiga, regla):
   
    total_colores = len(regla)
    color_actual = M[filaHormiga][columnaHormiga]
    siguiente_color = (color_actual + 1) % total_colores
    M[filaHormiga][columnaHormiga] = siguiente_color
    
    return M
def siguiente(M, filaHormiga, columnaHormiga, direccion, regla):
    
    color_actual = M[filaHormiga][columnaHormiga]
    giro = regla[color_actual]
    direccion = girar_hormiga(direccion, giro)
    M = transicion(M, filaHormiga, columnaHormiga, regla)
    total_filas = len(M)
    total_columnas = len(M[0])
    filaHormiga, columnaHormiga = avanzar_hormiga(filaHormiga, columnaHormiga, direccion, total_filas, total_columnas)
    
    return M, filaHormiga, columnaHormiga, direccion
