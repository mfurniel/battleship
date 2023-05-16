import creartablero
from clases.agente import Agente


tablero = creartablero.generar_tablero(10, 10) # Crea un tablero de 10x10
creartablero.agregar_barcos(tablero, [5, 4, 3, 3, 2]) # Agrega barcos de diferentes tamaños

creartablero.imprimirTableroSinCeros(tablero)

jugadorIA = Agente()
jugadorIA.greedy()
