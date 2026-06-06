from random import randint
import guiVida as gui


def generar_matriz_aleatoria(filas, columnas):
    """
    Propósito: generar una matriz con valores aleatorios (0 o 1) simulando células vivas y muertas.
    Entradas:
        filas: int
        columnas: int
    Restricciones:
        filas: int positivo mayor a 0.
        columnas: int positivo mayor a 0.
    Salidas:
        list (matriz bidimensional de enteros [0, 1])."""
    return [[randint(0, 1) for c in range(columnas)] for f in range(filas)]


def generar_matriz_vacia(filas, columnas):
    """
    Propósito: generar una matriz limpia con todas las posiciones en estado neutro (0).
    Entradas:
        filas: int
        columnas: int
    Restricciones:
        filas: int positivo mayor a 0.
        columnas: int positivo mayor a 0.
    Salidas:
        list (matriz bidimensional de enteros inicializados en 0)."""
    return [[0 for c in range(columnas)] for f in range(filas)]


def obtener_vecinos(M, f, c):
    """
    Propósito: extraer los estados de los 8 vecinos que rodean a una célula usando un entorno toroidal (borde conectado).
    Entradas:
        M: list (matriz bidimensional)
        f: int (índice de fila)
        c: int (índice de columna)
    Restricciones:
        M: debe ser una lista de listas no vacía.
        f: int (dentro del rango de filas de M).
        c: int (dentro del rango de columnas de M).
    Salidas:
        list (lista de 8 enteros con valores de los vecinos)."""
    vecinos=[]
    for i in range(f-1,f+2):
        for j in range(c-1,c+2):
            if not (i==f and j==c):
                k=i%len(M)
                l=j%len(M[0])
                vecinos.append(M[k][l])
    return vecinos


def transicion(M, b, s):
    """
    Propósito: calcular el estado de toda la matriz para la siguiente generación basándose en las reglas B y S.
    Entradas:
        M: list (matriz bidimensional)
        b: str (regla de nacimiento)
        s: str (regla de supervivencia)
    Restricciones:
        M: debe ser una lista de listas válida.
        b: str con dígitos del '0' al '8'.
        s: str con dígitos del '0' al '8'.
    Salidas:
        list (nueva matriz bidimensional calculada)."""
    newM=[]
    filis=[]
    for fila in range(len(M)):
        filis=[]
        for col in range(len(M[0])):
            veci=obtener_vecinos(M,fila,col)
            est=transicion_celula(M[fila][col],veci,b,s)
            filis.append(est)
        newM.append(filis)
    return newM


def transicion_celula(estado, vecinos, b, s):
    """
    Propósito: evaluar y retornar el próximo estado (0 o 1) de una célula individual según sus vecinos y las reglas dadas.
    Entradas:
        estado: int (0 o 1, estado actual de la célula)
        vecinos: list (lista de enteros con los 8 vecinos)
        b: str (regla de nacimiento)
        s: str (regla de supervivencia)
    Restricciones:
        estado: int con valor de 0 o 1.
        vecinos: list de exactamente 8 elementos enteros (0 o 1).
        b: str con dígitos del '0' al '8'.
        s: str con dígitos del '0' al '8'.
    Salidas:
        int (0 o 1 como resultado del nuevo estado)."""
    contador=0
    for vecino in vecinos:
        if vecino == 1:
            contador+=1
    contador=str(contador)
    if (contador in b) or (contador in s and estado==1):
        return 1
    else:
        return 0
