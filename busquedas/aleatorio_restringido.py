import random

def busqueda_aleatoria_restringida(self, rival):

    coordenadas = []
    for fila in range(10):
        for columna in range(10):
            if self.tableroBusqueda[fila][columna] == 0:
                coordenadas.append((fila, columna))

    random.shuffle(coordenadas)  # Desordenar las coordenadas
    turnos=0
    for coordenada in coordenadas:
        if(self.flota_rival_hundida()):
            # print('turnos azar: ',turnos)
            break
        turnos=turnos+1
        fila, columna = coordenada

        if self.pregunta(rival, fila, columna):
            self.tableroBusqueda[fila][columna] = 'X'
            self.turnos=self.turnos+1
            self.modo='target'
            self.coodenada_hunted = (fila,columna)
            break
        else:
            self.tableroBusqueda[fila][columna] = 'E'
            self.turnos=self.turnos+1
            break

   
