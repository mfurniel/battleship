
from busquedas import modo_target as hunt
import creartablero
def busqueda_greedy_hunt(self,rival):
  turnos = 0
  flag = False

  for i in range(10):
    for j in range(10):
      if(self.tableroBusqueda[i][j]=='X'):
        continue
      flag = self.flota_rival_hundida()
      print('x: ',j,' - y: ',i)
      # if(self.tableroBusqueda[i][j]=='E' or self.tableroBusqueda[i][j]=='X'):
      #   break
      # print(flag)
      # print(str(i),' ' , str(j) )
      turnos=turnos+1

      self.tableroBusqueda[i][j]='E'

      if(self.pregunta(rival,i,j)):

        self.tableroBusqueda[i][j]='X'
        hunt.target(i,j,self,rival)
        creartablero.imprimirTablero(self.tableroBusqueda)
        flag = self.flota_rival_hundida()
        
        # print(flag)

        if(flag):
          break
    if(flag):
      break
  
  #print('turnos: ' + str(turnos))

  
  return 0