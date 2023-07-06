import creartablero
from clases.agente import Agente
import versus

impirmirinicio = False


jugadorIA = Agente('IA')
jugadorRival = Agente('Rival')

matriz = [[0] * 10 for _ in range(10)]

# jugadorIA.cambiar_tablero_propio(matriz)

# ------- INICIO -------
if impirmirinicio:
    print('Jugador IA TABLERO PROPIO')
    creartablero.imprimirTablero(jugadorIA.tableroPropio)
    print('Jugador IA TABLERO BUSQUEDA')
    creartablero.imprimirTablero(jugadorIA.tableroBusqueda)

    print('Jugador RIVAL TABLERO PROPIO')
    creartablero.imprimirTablero(jugadorRival.tableroPropio)
    print('Jugador RIVAL TABLERO BUSQUEDA')
    creartablero.imprimirTablero(jugadorRival.tableroBusqueda)

print('Numero de Juegos\tCantidad de turnos')
# for i in range(100000):
#    del jugadorRival
#     del jugadorIA
#     jugadorIA = Agente('IA')
#     jugadorRival = Agente('Rival')  #Crear nuevo jugadorIA

#     versus.azar_vs_azar(jugadorIA,jugadorRival)

#     print(i+1,'\t',jugadorIA.turnos)

versus.heatMap_vs_huntTarget(jugadorIA, jugadorRival)

# ------- FINAL -------
print('Jugador IA TABLERO PROPIO')
creartablero.imprimirTablero(jugadorIA.tableroPropio)
print('Jugador IA TABLERO BUSQUEDA')
creartablero.imprimirTablero(jugadorIA.tableroBusqueda)

print('Jugador RIVAL TABLERO PROPIO')
creartablero.imprimirTablero(jugadorIA.tableroPropio)
print('Jugador RIVAL TABLERO BUSQUEDA')
creartablero.imprimirTablero(jugadorIA.tableroBusqueda)
