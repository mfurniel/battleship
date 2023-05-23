import random

class Direccion:
    def __init__(self, nombre, valido, direccion):
        self.nombre = nombre
        self.valido = valido
        self.direccion = direccion


def target(self,rival):
    coordenada_x, coordenada_y= self.coordenada_hunted
    print('coordanadas: ',coordenada_x,' ',coordenada_y)

    direcciones = [
    Direccion("Norte", False, (0, -1)),
    Direccion("Sur", False, (0, 1)),
    Direccion("Este", False, (1, 0)),
    Direccion("Oeste", False, (-1, 0))
    ]


    if (coordenada_x < 0 or coordenada_x >= 10 or coordenada_y < 0 or coordenada_y >= 10):
        print('coordenadas no validas')
        return 0
    
    verificar_direcciones(coordenada_x, coordenada_y, self.tableroBusqueda, direcciones)
    direcciones_validas = [direccion for direccion in direcciones if direccion.valido]

    #print('cantidad largos: ',len(direcciones_validas))

    nueva_coordenada_x = coordenada_x
    nueva_coordenada_y = coordenada_y

    while len(direcciones_validas)!=0:
        if(self.flota_rival_hundida()):
            break
        direcciones_validas = [direccion for direccion in direcciones if direccion.valido]
        print(len(direcciones_validas))
        for i in direcciones_validas:
            print(i.nombre)
        
        if(len(direcciones_validas)==0):
            break

        direccion_elegida = random.choice(direcciones_validas)
        #direccion_elegida.escogido = True  # Marcar la dirección como escogida

        print('direccion seleccionda: ',direccion_elegida.nombre)
       
        dx, dy = direccion_elegida.direccion
        nueva_coordenada_x, nueva_coordenada_y = nueva_coordenada_x + dx, nueva_coordenada_y + dy

        if nueva_coordenada_x < 0 or nueva_coordenada_x >= 10 or nueva_coordenada_y < 0 or nueva_coordenada_y >= 10:
            direccion_elegida.valido=False
            break 
 
        if(self.pregunta(rival,nueva_coordenada_x,nueva_coordenada_y)):
            
            self.tableroBusqueda[nueva_coordenada_x][nueva_coordenada_y]='X'
            while(direccion_elegida.valido):

                if(self.flota_rival_hundida()):
                    break 
                              
                nueva_coordenada_x, nueva_coordenada_y = nueva_coordenada_x + dx, nueva_coordenada_y + dy
                if nueva_coordenada_x < 0 or nueva_coordenada_x >= 10 or nueva_coordenada_y < 0 or nueva_coordenada_y >= 10:
                    direccion_elegida.valido=False
                    break 
                if(self.pregunta(rival,nueva_coordenada_x,nueva_coordenada_y)):
                    self.tableroBusqueda[nueva_coordenada_x][nueva_coordenada_y]='X'
                else:
                    self.tableroBusqueda[nueva_coordenada_x][nueva_coordenada_y]='E'    
                    direccion_elegida.valido=False
        else:
            if(self.flota_rival_hundida()):
                break
            self.tableroBusqueda[nueva_coordenada_x][nueva_coordenada_y]='E'    
            direccion_elegida.valido=False
            direcciones_validas = [direccion for direccion in direcciones if direccion.valido]
    else:
        print('No hay direcciones válidas')

    return 0

def verificar_direcciones(coordenada_x, coordenada_y, tablerobusqueda,direcciones):
      for direccion in direcciones:
        dx, dy = direccion.direccion
        new_x, new_y = coordenada_x + dx, coordenada_y + dy
        if new_x >= 0 and new_x < 10 and new_y >= 0 and new_y <= 10:
            if tablerobusqueda[new_x][new_y] == 0:
                direccion.valido = True
          
       
       
        



