def generar_ramatriz(filas, columnas):
    """ matriz puros 0s"""

    return [[0 for c in range (columnas)] for f in range(filas)]

def girar_hormiga(orientacion_actual, giro):
    
    giro_derecha = {"U": "R", "R": "D", "D": "L", "L": "U"}
    giro_izquierda = {"U": "L", "L": "D", "D": "R", "R": "U"}
    
    if giro == "R":
        return giro_derecha[orientacion_actual]
    else:
        return giro_izquierda[orientacion_actual]

        
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
