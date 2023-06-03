import creartablero
from clases.agente import Agente
import versus


#tablero = creartablero.generar_tablero(10, 10) # Crea un tablero de 10x10
#creartablero.agregar_barcos(tablero, [5, 4, 3, 3, 2]) # Agrega barcos de diferentes tamaños

matriz = [[0] * 10 for _ in range(10)]  # Crear una matriz de 10x10 con elementos inicializados a 0
matriz1 = [[0] * 10 for _ in range(10)]
for i in range(len(matriz)):
    matriz[i][0] = 1
    matriz[i][1] = 1
    matriz[9][1]=0
    matriz[8][1]=0
    matriz[7][1]=0
for i in range(len(matriz)):
    matriz1[i][0] = 1
    matriz1[i][1] = 1
    matriz1[9][1]=0
    matriz1[8][1]=0
    matriz1[7][1]=0

jugadorIA = Agente('IA')
jugadorRival = Agente('Rival')
# jugadorIA.cambiar_tablero_propio(matriz)
# jugadorRival.cambiar_tablero_propio(matriz1)


creartablero.imprimirTableroSinCeros(jugadorIA.tableroPropio)
print('   S - E - P - A - R - A - C - I - O - N   ')
creartablero.imprimirTableroSinCeros(jugadorRival.tableroPropio)

#versus.azar_vs_azar(jugadorIA,jugadorRival)

#versus.greedy_vs_azar(jugadorIA,jugadorRival)


versus.huntTarget_vs_huntTarget(jugadorIA,jugadorRival)
#versus.greedy_vs_greedy(jugadorIA,jugadorRival)

#creartablero.imprimirTableroSinCeros(jugadorIA.tableroPropio)
#print('   S - E - P - A - R - A - C - I - O - N   ')
creartablero.imprimirTableroSinCeros(jugadorRival.tableroPropio)
print('   S - E - P - A - R - A - C - I - O - N    PROPRIO RIVAL - BUSQUEDA IA')
creartablero.imprimirTablero(jugadorIA.tableroBusqueda)
print('   S - E - P - A - R - A - C - I - O - N    MITAD')
creartablero.imprimirTableroSinCeros(jugadorIA.tableroPropio)
print('   S - E - P - A - R - A - C - I - O - N    PROPRIO IA - BUSQUEDA RIVAL')
creartablero.imprimirTablero(jugadorRival.tableroBusqueda)
#print('   S - E - P - A - R - A - C - I - O - N   ')
#creartablero.imprimirTablero(jugadorRival.tableroBusqueda)


# jugadorRival.cambiar_tablero_propio(matriz)

# creartablero.imprimirTablero(jugadorRival.tableroPropio)
# print('___________SEPARACION___________')
# creartablero.imprimirTablero(jugadorIA.tableroBusqueda)
# media=0
# for i in range(1):
#     jugadorIA = Agente()
#     media=media + jugadorIA.aleatoriopero(jugadorRival)
#     print(jugadorIA.turnos)
# media=media/1
# print('media :',media)
# jugadorIA.greedy_hunt(jugadorRival)
# creartablero.imprimirTablero(jugadorIA.tableroBusqueda)

#para aleatorio voy a usar y para diferenciar que hizo greedy y que hizo aleatorio
#jugadorIA.aleatorio(jugadorRival)

#creartablero.imprimirTablero(jugadorIA.tablerobBusqueda)
#game





#jugadorIA.greedy(tablero)

#nose si esto esta funcionado bien aiuda

