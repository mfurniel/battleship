
def busqueda_greedy(self,rival):
  flag = False

  for i in range(10):
    for j in range(10):
      if(self.flota_rival_hundida()):
        break
      if(self.tableroBusqueda[i][j]==0):
        # self.turnos=self.turnos+1
        
        if(self.pregunta(rival,i,j)):
          self.tableroBusqueda[i][j]='X'
          flag=True
          self.modo='target'
          self.coodenada_hunted = (i,j)
          break
        else:
          self.tableroBusqueda[i][j]='E'
          flag=True
          break

    if(flag):
      break    
 

