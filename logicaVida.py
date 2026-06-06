from random import randint
import guiVida as gui


def generar_matriz_aleatoria(filas, columnas):
    """Función que retorna una matriz de las dimensiones
    especificadas con valores enteros aleatorios de 0 o 1"""
    return [[randint(0, 1) for c in range(columnas)] for f in range(filas)]
def generar_matriz_vacia(filas, columnas):
    """Función que retorna una matriz de las dimensiones
    especificadas con valores enteros aleatorios de 0 o 1"""
    return [[0 for c in range(columnas)] for f in range(filas)]
def obtener_vecinos(M, f, c):
    """Función que retorna una lista con los estados de
    los 8 vecinos de la célula en la posición f, c de M."""
    vecinos=[]
    for i in range(f-1,f+2):
        for j in range(c-1,c+2):
            if not (i==f and j==c):
                k=i%len(M)
                l=j%len(M[0])
                vecinos.append(M[k][l])
    return vecinos
def transicion(M, b, s):
    """Toma a la matriz completa y le aplica la función de
    transición a cada célula con su propio vecindario y deja
    el resultado en una matriz nueva."""
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
    """Retorna el nuevo estado de la célula de acuerdo
    al estado de sus vecinos."""
    contador=0
    for vecino in vecinos:
        if vecino == 1:
            contador+=1
    contador=str(contador)
    if (contador in b) or (contador in s and estado==1):
        return 1
    else:
        return 0    


