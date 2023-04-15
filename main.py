import funciones as func
tablero1 = [[ 0 for j in range(10)] for i in range(10)]
#func.imprimirTablero(tablero1)
tablero = func.generar_tablero(10, 10) # Crea un tablero de 10x10
func.agregar_barcos(tablero, [5, 4, 3, 3, 2]) # Agrega barcos de diferentes tamaños
func.imprimirTableroSinCeros(tablero)