import random

class Direccion:
    def __init__(self, nombre, valido, direccion):
        self.nombre = nombre
        self.valido = valido
        self.direccion = direccion
        self.escogido = False


def hunt_target(coordenada_x,coordenada_y,tablerobusqueda,tablerorival):

    direcciones = [
    Direccion("Norte", True, (0, 1)),
    Direccion("Sur", True, (0, -1)),
    Direccion("Este", True, (1, 0)),
    Direccion("Oeste", True, (-1, 0))
    ]

    #verificamos si las coordenadas no estan fuera del tablero
    if (coordenada_x < 0 or coordenada_x >= 10 or coordenada_y < 0 or coordenada_y >= 10):
        print('coordenadas no validas')
        return
    
    verificar_direcciones(coordenada_x, coordenada_y, tablerobusqueda, direcciones)

    direcciones_validas = [direccion for direccion in direcciones if direccion.valido and not direccion.escogido]
    
    if direcciones_validas:
        # Elegir aleatoriamente una dirección válida no escogida
        direccion_elegida = random.choice(direcciones_validas)
        direccion_elegida.escogido = True  # Marcar la dirección como escogida
        
        # Obtener las coordenadas de la dirección elegida
        dx, dy = direccion_elegida.direccion
        nueva_coordenada_x, nueva_coordenada_y = coordenada_x + dx, coordenada_y + dy
        
        # Realizar acciones con la dirección elegida
        # ...
    else:
        print('No hay direcciones válidas no escogidas')

    
                

    #casos posibles
    #verificar las casillas norte, sur, este y oeste
        #si estan dentro del tablero
        #escojemos una casilla 
            #aleatoriamente?
            #en orden? norte,sur,este,oeste
            #una combinacion?
            #si se escoje aleatoriamente norte se escoje enre oeste o este
                #se podria escojer dependiendoo de la cantidad de casillas hacia tal o cual direccion (quien tenga mas casillas a los lados)
    #una vez escojida la direccion avanzamos hasta que no encotremos casillas marcadas
    #si ya no puede avanzar mas se verficia desde la casilla de origen a la direccion contraria

    return 0

def verificar_direcciones(coordenada_x, coordenada_y, tablerobusqueda,direcciones):
      for direccion in direcciones:
        dx, dy = direccion.direccion
        new_x, new_y = coordenada_x + dx, coordenada_y + dy

        # Verificar si las nuevas coordenadas están dentro del tablero
        if new_x < 0 or new_x >= 10 or new_y < 0 or new_y >= 10:
            direccion.valido = False  # Casilla fuera del tablero
        elif tablerobusqueda[new_x][new_y] != 'E' or tablerobusqueda[new_x][new_y] == 'X':
            direccion.valido = False  # Casilla no válida (ya explorada)





