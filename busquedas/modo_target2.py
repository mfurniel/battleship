from clases import direccion as cardinal
import random



def target(self,rival):
    
    if(self.flota_rival_hundida()):
        return 0
    
    fila = self.coordenada_hunted[1]
    columna = self.coordenada_hunted[0]
    # print('x: ',fila,'y: ' ,columna)
    if not coordendas_dentro_tablero(fila,columna):
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
            direcciones.append(cardinal.Direccion("Norte", True, (0, -1))) # columna fila
        if(self.direccion_target=='Sur'):
            direcciones.append(cardinal.Direccion("Sur", True, (0, 1))) # columna fila
        if(self.direccion_target=='Este'):
            direcciones.append(cardinal.Direccion("Este", True, (1, 0))) # columna fila
        if(self.direccion_target=='Oeste'):
            direcciones.append(cardinal.Direccion("Oeste", True, (-1, 0))) # columna fila     

    #for i in direcciones:
        #print(i.nombre)
    #print('b')
    #print('cantidad largos: ',len(direcciones_validas))
    
    direcciones_validas = [direccion for direccion in direcciones if direccion.valido]

    nueva_fila = fila
    nueva_columna = columna

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

        nueva_fila, nueva_columna = nueva_fila + direccion_elegida.direccion[1], nueva_columna + direccion_elegida.direccion[0]
        if(self.nombre=='IA'):
            print('direccion elegida: ',direccion_elegida.nombre)
            print('x: ',fila,'y: ',columna)
            print('suma en x: ', direccion_elegida.direccion[0],'suma en y: ',direccion_elegida.direccion[1])
            print('nueva x: ',nueva_fila,'nueva y: ',nueva_columna)


        if nueva_fila < 0 or nueva_fila >= 10 or nueva_columna < 0 or nueva_columna >= 10:
            print('no esta dentro del tablero')
            direccion_elegida.valido=False
            direcciones_validas = [direccion for direccion in direcciones if direccion.valido]
            continue
        
        if self.tableroBusqueda[nueva_columna][nueva_fila]!=0:
            print('es distinto de 0')
            direccion_elegida.valido=False
            direcciones_validas = [direccion for direccion in direcciones if direccion.valido]
            continue 
 
        if self.pregunta(rival,nueva_columna,nueva_fila):
            print('al parecer acerto')
            self.tableroBusqueda[nueva_columna][nueva_fila]='X'
            self.coordenada_hunted=nueva_columna,nueva_fila
            self.modo='target'
            self.direccion_target=direccion_elegida.nombre
            return 0
        else:
            self.tableroBusqueda[nueva_columna][nueva_fila]='E'
            self.coordenada_hunted=nueva_columna,nueva_fila
            self.modo='hunt'
            self.direccion_target='none'
            return 0

    if len(direcciones_validas)==0:
        self.modo='hunt'
        self.direccion_target='none'
        print('No hay direcciones validas')

    return 0

def verificar_direcciones(columna, fila, tablerobusqueda,direcciones):
      for direccion in direcciones:
        dx, dy = direccion.direccion
        new_columna, new_fila = columna + dx, fila + dy
        if new_columna >= 0 and new_columna < 10 and new_fila >= 0 and new_fila < 10:
            if tablerobusqueda[new_columna][new_fila] == 0:
                direccion.valido = True
          
def coordendas_dentro_tablero(fila,columna):
      if (fila < 0 or fila >= 10 or columna < 0 or columna >= 10):
        return False
      else:
        return True      
       
def direcciones_elegidas(self):

    direcciones = [
    cardinal.Direccion("Norte", False, (0, -1)), #columna fila
    cardinal.Direccion("Sur", False, (0, 1)),   #columna fila
    cardinal.Direccion("Este", False, (1, 0)),  #columna fila
    cardinal.Direccion("Oeste", False, (-1, 0)) #columna fila
    ]

    direcciones_validas = []

    fila, columna= self.coordenada_hunted
   
    if not coordendas_dentro_tablero(columna,fila):
        return direcciones_validas
    
    verificar_direcciones(columna, fila, self.tableroBusqueda, direcciones)

    direcciones_validas = [direccion for direccion in direcciones if direccion.valido]

    return direcciones_validas
