import creartablero
from clases.agente import Agente
import versus


#tablero = creartablero.generar_tablero(10, 10) # Crea un tablero de 10x10
#creartablero.agregar_barcos(tablero, [5, 4, 3, 3, 2]) # Agrega barcos de diferentes tamaños
matriz = [[0] * 10 for  _ in range(10)]  # Crear una matriz de 10x10 con elementos inicializados a 0
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


jugadorIA = Agente()
jugadorRival = Agente()
jugadorRival.cambiar_tablero_propio(matriz)
jugadorIA.greedy(jugadorRival)
print("tablero original")
creartablero.imprimirTablero(jugadorRival.tableroPropio)
print("tablero con Greedy")
creartablero.imprimirTablero(jugadorIA.tablerobBusqueda)

#para aleatorio voy a usar y para diferenciar que hizo greedy y que hizo aleatorio
#jugadorIA.aleatorio(jugadorRival)

creartablero.imprimirTablero(jugadorIA.tablerobBusqueda)
#game





#jugadorIA.greedy(tablero)

#nose si esto esta funcionado bien aiuda

