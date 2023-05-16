def imprimirTablero(matriz):
    if len(matriz) == 0:
        print("La matriz está vacía.")
        return
    
    # Calcular la longitud máxima de los elementos de la matriz
    ancho = max(len(str(elemento)) for fila in matriz for elemento in fila)
    
    # Imprimir la matriz con bordes
    print("+" + ("-" * (ancho + 2) + "+") * len(matriz[0]))
    for fila in matriz:
        for elemento in fila:
            print("| {:^{ancho}} ".format(elemento, ancho=ancho), end="")
        print("|")
        print("+" + ("-" * (ancho + 2) + "+") * len(matriz[0]))

def imprimirTableroSinCeros(matriz):
    if len(matriz) == 0:
        print("La matriz está vacía.")
        return
    
    # Calcular la longitud máxima de los elementos de la matriz
    ancho = max(len(str(elemento)) for fila in matriz for elemento in fila)
    
    # Imprimir la matriz con bordes
    print("+" + ("-" * (ancho + 2) + "+") * len(matriz[0]))
    for fila in matriz:
        for elemento in fila:
            if elemento == 0:
                print("| {:^{ancho}} ".format(" ", ancho=ancho), end="")
            else:
                print("| {:^{ancho}} ".format(elemento, ancho=ancho), end="")
        print("|")
        print("+" + ("-" * (ancho + 2) + "+") * len(matriz[0]))


import random

def generar_tablero(filas, columnas):
    tablero = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            fila.append(0)
        tablero.append(fila)
    return tablero

def agregar_barco(tablero, tamano, fila, columna, orientacion, barcos_agregados):
    if orientacion == 'horizontal':
        for i in range(tamano):
            if (fila, columna + i) in barcos_agregados:
                return False
        for i in range(tamano):
            tablero[fila][columna + i] = 1
            barcos_agregados.append((fila, columna + i))
        return True
    else:
        for i in range(tamano):
            if (fila + i, columna) in barcos_agregados:
                return False
        for i in range(tamano):
            tablero[fila + i][columna] = 1
            barcos_agregados.append((fila + i, columna))
        return True

def agregar_barcos(tablero, tamano_barcos):
    barcos_agregados = []
    for tamano in tamano_barcos:
        barco_agregado = False
        while not barco_agregado:
            orientacion = random.choice(['horizontal', 'vertical'])
            if orientacion == 'horizontal':
                fila = random.randint(0, len(tablero) - 1)
                columna = random.randint(0, len(tablero[0]) - tamano)
            else:
                fila = random.randint(0, len(tablero) - tamano)
                columna = random.randint(0, len(tablero[0]) - 1)
            barco_agregado = agregar_barco(tablero, tamano, fila, columna, orientacion, barcos_agregados)

