import random
def busqueda_aleatoria(self,rival):
    for i in range(10):
      for j in range(10):
        if self.tablerobBusqueda[i][j]=='E':
          self.tablerobBusqueda[i][j]= 0


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
      if fila_aleatoria-1-i < 0: break
     else:
       break
    return 0

def hundir_abajo(self,rival, fila_aleatoria, columna_aleatoria): 
    for i in range(0, 6):
     if self.pregunta(rival, fila_aleatoria + i,columna_aleatoria):
      self.tablerobBusqueda[fila_aleatoria + i][columna_aleatoria]='Y'
      if fila_aleatoria+1+i > 9: break
     else:
       break
    return 0

def hundir_derecha(self,rival, fila_aleatoria, columna_aleatoria): 
    for i in range(0, 6):
     if self.pregunta(rival, fila_aleatoria,columna_aleatoria + i):
      self.tablerobBusqueda[fila_aleatoria][columna_aleatoria + i]='Y'
      if columna_aleatoria+1+i > 9: break
     else:
      break
    return 0

def hundir_izquierda(self,rival, fila_aleatoria, columna_aleatoria): 
    for i in range(1, 6):
     if self.pregunta(rival, fila_aleatoria,columna_aleatoria - i):
      self.tablerobBusqueda[fila_aleatoria][columna_aleatoria - i]='Y'
      if columna_aleatoria-1-i < 0: break
     else:
       break
    return 0