import random

def busqueda_aleatoria_restringida(self, rival):

    coordenadas = []
    for fila in range(10):
        for columna in range(10):
            if self.tableroBusqueda[fila][columna] == 0:
                coordenadas.append((fila, columna))

    random.shuffle(coordenadas)  # Desordenar las coordenadas

    for coordenada in coordenadas:
        if(self.flota_rival_hundida()):
            # print('turnos azar: ',turnos)
            break
       
        fila, columna = coordenada

        if self.pregunta(rival, fila, columna):
            self.tableroBusqueda[fila][columna] = 'X'
            self.coordenada_hunted = (columna,fila)
            self.modo='target'
            self.coodenada_hunted = (fila,columna)
            self.turnos=self.turnos + 1
            break
        else:
            self.tableroBusqueda[fila][columna] = 'E'
            self.turnos=self.turnos + 1
            break

   
