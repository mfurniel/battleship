import random
def busqueda_aleatoria(self,rival):
    print(" esto es busqueda aleatoria")
    for i in range(0,99):
      fila_aleatoria = random.randint(0,9)
      columna_aleatoria = random.randint(0,9)
      if self.pregunta(rival, fila_aleatoria,columna_aleatoria):
        print(" fila ", fila_aleatoria, " columna ", columna_aleatoria)
        print(self.pregunta(rival, fila_aleatoria,columna_aleatoria))
        self.tablerobBusqueda[fila_aleatoria][columna_aleatoria]='Y'
        hundir_arriba(self,rival,fila_aleatoria,columna_aleatoria)
        hundir_abajo(self,rival,fila_aleatoria,columna_aleatoria)
        hundir_izquierda(self,rival,fila_aleatoria,columna_aleatoria)
        hundir_derecha(self,rival,fila_aleatoria,columna_aleatoria)
        
    return 0
    
def hundir_arriba(self,rival, fila_aleatoria, columna_aleatoria): 
    for i in range(1, 6):
     if self.pregunta(rival, fila_aleatoria - i,columna_aleatoria):
      self.tablerobBusqueda[fila_aleatoria - i][columna_aleatoria]='Y'
     else:
       break
    return 0

def hundir_abajo(self,rival, fila_aleatoria, columna_aleatoria): 
    for i in range(1, 6):
     if self.pregunta(rival, fila_aleatoria + i,columna_aleatoria):
      self.tablerobBusqueda[fila_aleatoria + i][columna_aleatoria]='Y'
     else:
       break
    return 0

def hundir_derecha(self,rival, fila_aleatoria, columna_aleatoria): 
    for i in range(1, 6):
     if self.pregunta(rival, fila_aleatoria,columna_aleatoria + i):
      self.tablerobBusqueda[fila_aleatoria][columna_aleatoria + i]='Y'
     else:
      break
    return 0

def hundir_izquierda(self,rival, fila_aleatoria, columna_aleatoria): 
    for i in range(1, 6):
     if self.pregunta(rival, fila_aleatoria,columna_aleatoria - i):
      self.tablerobBusqueda[fila_aleatoria][columna_aleatoria - i]='Y'
     else:
       break
    return 0