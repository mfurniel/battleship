import creartablero
from clases.agente import Agente
import versus

impirmirinicio=False

jugadorIA = Agente('IA')
jugadorRival = Agente('Rival')

#------- INICIO -------
if impirmirinicio:
    print('Jugador IA TABLERO PROPIO')
    creartablero.imprimirTablero(jugadorIA.tableroPropio)
    print('Jugador IA TABLERO BUSQUEDA')
    creartablero.imprimirTablero(jugadorIA.tableroBusqueda)

    print('Jugador RIVAL TABLERO PROPIO')
    creartablero.imprimirTablero(jugadorRival.tableroPropio)
    print('Jugador RIVAL TABLERO BUSQUEDA')
    creartablero.imprimirTablero(jugadorRival.tableroBusqueda)

versus.huntTarget_vs_huntTarget(jugadorIA,jugadorRival)

#------- FINAL -------
# print('Jugador IA TABLERO PROPIO')
# creartablero.imprimirTablero(jugadorIA.tableroPropio)
# print('Jugador IA TABLERO BUSQUEDA')
# creartablero.imprimirTablero(jugadorIA.tableroBusqueda)

# print('Jugador RIVAL TABLERO PROPIO')
# creartablero.imprimirTablero(jugadorIA.tableroPropio)
# print('Jugador RIVAL TABLERO BUSQUEDA')
# creartablero.imprimirTablero(jugadorIA.tableroBusqueda)