
def busqueda_greedy(self,rival):
  turnos = 0
  flag = False

  for i in range(10):
    for j in range(10):
      print(flag)
      print(str(i),' ' , str(j) )
      turnos=turnos+1
      if(self.pregunta(rival,i,j)):
        self.tablerobBusqueda[i][j]='X'
        flag = self.flota_rival_hundida()
        print(flag)
        if(flag):
          break
    if(flag):
      break
  
  print('turnos: ' + str(turnos))

  return 0