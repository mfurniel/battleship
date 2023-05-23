from clases import direccion as cardinal
import random



def target(self,rival):

    if(self.flota_rival_hundida()):
        return 0
    
    coordenada_x = self.coordenada_hunted[0]
    coordenada_y = self.coordenada_hunted[1]
    # print('x: ',coordenada_x,'y: ' ,coordenada_y)
    if not coordendas_dentro_tablero(coordenada_x,coordenada_y):
        self.modo='hunt'
        self.direccion_target='none'
        #print('fuera1')
        return 0
    #print('a')
    direcciones = []
    if(self.direccion_target=='none'):
        direcciones=direcciones_elegidas(self)
    else:
        if(self.direccion_target=='Norte'):
            direcciones.append(cardinal.Direccion("Norte", True, (0, -1)))
        if(self.direccion_target=='Sur'):
            direcciones.append(cardinal.Direccion("Sur", True, (0, 1)))
        if(self.direccion_target=='Este'):
            direcciones.append(cardinal.Direccion("Este", True, (1, 0)))
        if(self.direccion_target=='Oeste'):
            direcciones.append(cardinal.Direccion("Oeste", True, (-1, 0)))    

    #for i in direcciones:
        #print(i.nombre)
    #print('b')
    #print('cantidad largos: ',len(direcciones_validas))
    
    direcciones_validas = [direccion for direccion in direcciones if direccion.valido]

    nueva_coordenada_x = coordenada_x
    nueva_coordenada_y = coordenada_y

    #print('c')
    while len(direcciones_validas)!=0:

        if(self.flota_rival_hundida()):
            break
        #print('d inicio while')


        direcciones_validas = [direccion for direccion in direcciones if direccion.valido]

        if len(direcciones_validas)==0:
            self.modo='hunt'
            self.direccion_target='none'
            break

        direccion_elegida = random.choice(direcciones_validas)

        #for i in direcciones:
            #print('d - ',i.nombre)

        nueva_coordenada_x, nueva_coordenada_y = nueva_coordenada_x + direccion_elegida.direccion[0], nueva_coordenada_y + direccion_elegida.direccion[1]

        if nueva_coordenada_x < 0 or nueva_coordenada_x >= 10 or nueva_coordenada_y < 0 or nueva_coordenada_y >= 10:
            direccion_elegida.valido=False
            direcciones_validas = [direccion for direccion in direcciones if direccion.valido]
            continue
        
        if self.tableroBusqueda[nueva_coordenada_x][nueva_coordenada_y]!=0:
            direccion_elegida.valido=False
            direcciones_validas = [direccion for direccion in direcciones if direccion.valido]
            continue 
 
        if self.pregunta(rival,nueva_coordenada_x,nueva_coordenada_y):

            self.tableroBusqueda[nueva_coordenada_x][nueva_coordenada_y]='X'
            self.coordenada_hunted=nueva_coordenada_x,nueva_coordenada_y
            self.modo='target'
            self.direccion_target=direccion_elegida.nombre
            break

        else:

            self.tableroBusqueda[nueva_coordenada_x][nueva_coordenada_y]='E'
            self.modo='hunt'
            self.direccion_target='none'
            break

    if len(direcciones_validas)==0:
        self.modo='hunt'
        self.direccion_target='none'
        print('No hay direcciones válidas')

    return 0

def verificar_direcciones(coordenada_x, coordenada_y, tablerobusqueda,direcciones):
      for direccion in direcciones:
        dx, dy = direccion.direccion
        new_x, new_y = coordenada_x + dx, coordenada_y + dy
        if new_x >= 0 and new_x < 10 and new_y >= 0 and new_y < 10:
            if tablerobusqueda[new_x][new_y] == 0:
                direccion.valido = True
          
def coordendas_dentro_tablero(coordenada_x,coordenada_y):
      if (coordenada_x < 0 or coordenada_x >= 10 or coordenada_y < 0 or coordenada_y >= 10):
        return False
      else:
        return True      
       
def direcciones_elegidas(self):

    direcciones = [
    cardinal.Direccion("Norte", False, (0, -1)),
    cardinal.Direccion("Sur", False, (0, 1)),
    cardinal.Direccion("Este", False, (1, 0)),
    cardinal.Direccion("Oeste", False, (-1, 0))
    ]

    direcciones_validas = []

    coordenada_x, coordenada_y= self.coordenada_hunted
   

    if not coordendas_dentro_tablero(coordenada_x,coordenada_y):
        return direcciones_validas
    
    verificar_direcciones(coordenada_x, coordenada_y, self.tableroBusqueda, direcciones)

    direcciones_validas = [direccion for direccion in direcciones if direccion.valido]

    return direcciones_validas
