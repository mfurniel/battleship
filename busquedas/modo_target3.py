from clases import direccion as cardinal
import random

def neo_target(self,rival):
    #revisar si la flota esta hundida? no deberia en teoria
    #revisamos si las coordenadas se encuentran dentro del tablero? deberian siempre estar dentro la verdad
    nueva_x=self.coordenada_hunted[0]
    nueva_y=self.coordenada_hunted[1]

    direcciones = []
    if(self.direccion_target=='none'):
        direcciones=direcciones_elegidas(self)
    else:
        if(self.direccion_target=='Norte'):
            direcciones.append(cardinal.Direccion("Norte", True, (0, -1))) # columna fila; lo vemos como coordanda x y
        if(self.direccion_target=='Sur'):
            direcciones.append(cardinal.Direccion("Sur", True, (0, 1))) # columna fila; lo vemos como coordanda x y
        if(self.direccion_target=='Este'):
            direcciones.append(cardinal.Direccion("Este", True, (1, 0))) # columna fila; lo vemos como coordanda x y
        if(self.direccion_target=='Oeste'):
            direcciones.append(cardinal.Direccion("Oeste", True, (-1, 0))) # columna fila; lo vemos como coordanda x y 

    direcciones_validas = [direccion for direccion in direcciones if direccion.valido]
    
    while(len(direcciones_validas)!=0):

        direcciones_validas = [direccion for direccion in direcciones if direccion.valido]
        direccion_elegida = random.choice(direcciones_validas)
        nueva_x, nueva_y = nueva_x + direccion_elegida.direccion[0], nueva_y + direccion_elegida.direccion[1]

        if(self.nombre=='IA'):
            for a in direcciones_validas:
                print('direcciones validas: ',a.nombre)
            print('direccion elegida: ',direccion_elegida.nombre)
            print('x: ',self.coordenada_hunted[0],'y: ',self.coordenada_hunted[1])
            print('direccion x: ', direccion_elegida.direccion[0],'direccion y: ',direccion_elegida.direccion[1])
            print('neo x: ',nueva_x,'neo y: ',nueva_y)

        if nueva_x < 0 or nueva_x >= 10 or nueva_y < 0 or nueva_y >= 10:
            if(self.nombre=='IA'):
                print('no esta dentro del tablero')
            direccion_elegida.valido=False
            direcciones_validas = [direccion for direccion in direcciones if direccion.valido]
            continue

        if self.tableroBusqueda[nueva_y][nueva_x]!=0:
            if(self.nombre=='IA'):
                print('es distinto de 0')
            direccion_elegida.valido=False
            direcciones_validas = [direccion for direccion in direcciones if direccion.valido]
            continue 

        if self.pregunta(rival,nueva_y,nueva_x):
            if(self.nombre=='IA'):
                print('al parecer acerto')
            self.tableroBusqueda[nueva_y][nueva_x]='X'
            self.coordenada_hunted=nueva_x,nueva_y
            self.modo='target'
            self.direccion_target=direccion_elegida.nombre
            return 0
        else: #arreglar aca!!!! ha qe guardar las direcciones o algo asi
            if(self.nombre=='IA'):
                print('no acerto y puso E')
            self.tableroBusqueda[nueva_y][nueva_x]='E'
            direccion_elegida.valido=False
            direcciones_validas = [direccion for direccion in direcciones if direccion.valido]
            self.direccion_target='none'
            self.modo='hunt'
            # if len(direcciones_validas)==0:
            #     print('E pero no hay mas direcciones')
            #     for a in direcciones_validas:
            #         print(a.nombre)
            #     self.modo='hunt'
            #     self.coordenada_hunted = (0, 0)
            #     self.direccion_target='none'
            return 0
        
    if(self.nombre=='IA'):
        print('no hay direcciones y volvemos al modo hunt')
    self.modo='hunt'
    self.coordenada_hunted = (0, 0)
    self.direccion_target='none'
    return 0

def direcciones_elegidas(self):

    direcciones = [
    cardinal.Direccion("Norte", False, (0, -1)), #columna fila; lo vemos como coordanda x y
    cardinal.Direccion("Sur", False, (0, 1)),   #columna fila; lo vemos como coordanda x y
    cardinal.Direccion("Este", False, (1, 0)),  #columna fila; lo vemos como coordanda x y
    cardinal.Direccion("Oeste", False, (-1, 0)) #columna fila; lo vemos como coordanda x y
    ]

    direcciones_validas = []

    x, y= self.coordenada_hunted
   
    if not coordendas_dentro_tablero(x,y):
        return direcciones_validas
    
    verificar_direcciones(self,x, y, self.tableroBusqueda, direcciones) #aqui hay algo que no entiendo pero parece que funca si es x la fila o la columna aaahhh

    direcciones_validas = [direccion for direccion in direcciones if direccion.valido]

    return direcciones_validas

def verificar_direcciones(self,fila, columna, tablerobusqueda,direcciones):
    # print('-verificando direcciones validas-')
    for direccion in direcciones:
        if(self.nombre=='IA'):
            print(direccion.nombre)
        d_columna, d_fila = direccion.direccion
        if(self.nombre=='IA'):
            print('valor columna: ',d_columna,'valor fila: ',d_fila)
        new_columna, new_fila = columna + d_fila, fila + d_columna
        if(self.nombre=='IA'):
            print(columna,' + ',d_columna,' = ',new_columna)
            print(fila,' + ',d_fila,' = ',d_fila)
        if new_columna >= 0 and new_columna < 10 and new_fila >= 0 and new_fila < 10:
            if(self.nombre=='IA'):        
                print('tablerodebusqueda[',new_columna,']','[',new_fila,']')
            if tablerobusqueda[new_columna][new_fila] == 0:
                if(self.nombre=='IA'):
                    print('cumple')
                direccion.valido = True
            else:
                if self.nombre=='IA':
                    print('valor no es 0')
    print('--verificando direcciones validas--')


#En esta fucnion no importa si x es fila o columna ya que si nose cumple esto funciona
# igual; adema nos aprovechamos del hecho de que es un tablero de 10x10 osea cuadrado 
def coordendas_dentro_tablero(x,y):
      if (x < 0 or x >= 10 or y < 0 or y >= 10):
        return False
      else:
        return True 