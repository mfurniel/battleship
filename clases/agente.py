from clases import barco 
import creartablero
from busquedas.greedy import busqueda_greedy 
from busquedas.greedy_hunt import busqueda_greedy_hunt
from busquedas.aleatorio import busqueda_aleatoria
from busquedas.aleatorio_restringido import busqueda_aleatoria_restringida
from busquedas.modo_target2 import target


class Agente:
    def __init__(self,nombre):
        self.nombre=nombre
        self.tableroBusqueda = [[0] * 10 for _ in range(10)]
        self.tableroPropio = creartablero.generar_tablero(10, 10)
        self.memoria = []
        self.turnos=0
        self.modo='hunt'
        self.coordenada_hunted=(0,0)
        self.direccion_target='none'
        self.agregar_barcos_predeterminados()
        creartablero.agregar_barcos(self.tableroPropio, [5, 4, 3, 3, 2])

    def agregar_barcos_predeterminados(self):
        barcos = [
            barco.Barco("Portaaviones", 5),
            barco.Barco("Acorazado", 4),
            barco.Barco("Destructor", 3),
            barco.Barco("Submarino", 3),
            barco.Barco("Bote", 2)
        ]
        self.memoria.extend(barcos)

    #la idea era identificar el barco en si, pero podria darse el caso
    #en que no se pueda distinguir si es tal o cual barco, si estan juntos,
    #podria ser buena idea revisae eso si

    # def flota_rival_hundida1(self):
    #     for i in self.memoria:
    #         if(i.encontrado==False):
    #             return False
    #     return True   
    
    def flota_rival_hundida(self):
        count_x = sum(row.count('X') for row in self.tableroBusqueda)
        if(count_x == 17):
            return True
        return False  
    
    def pregunta(self,rival,coordenada_x,coordenada_y):
        return rival.respuesta(rival,coordenada_x,coordenada_y)

    def respuesta(self,rival,coordenada_x,coordenada_y):
        if(rival.tableroPropio[coordenada_x][coordenada_y]==0):
            return False
        if(rival.tableroPropio[coordenada_x][coordenada_y]==1):
            return True
        return False
    
    def cambiar_tablero_propio(self,tablero):
        self.tableroPropio=tablero

    def cuantos(self):
       count_x = sum(row.count('X') for row in self.tableroBusqueda)
       return count_x
      
    
    #LA idea seria agregar aqui las busquedas

    def greedy(self,rival):
        busqueda_greedy(self,rival)
    
    def greedy_hunt(self,rival):
        busqueda_greedy_hunt(self,rival)

    def aleatorio(self,rival):
        busqueda_aleatoria(self,rival)
    
    def aleatorio_restringido(self,rival):
        busqueda_aleatoria_restringida(self,rival)

    def hunt_target(self,rival,busqueda_hunt):
        # print(self.nombre,' - ',self.modo,' - ',self.direccion_target)
        # print(self.coordenada_hunted)
        # if(self.modo=='hunt'):

        # if(self.nombre=='IA'):   
        #      print(self.direccion_target)

        if(busqueda_hunt=='greedy'):
                busqueda_greedy(self,rival)
        if(busqueda_hunt=='aleatorio'):
                busqueda_aleatoria(self,rival)
        if(busqueda_hunt=='aleatorio_restringido'):
                busqueda_aleatoria_restringida(self,rival)
            
            #print('hunt')

        elif(self.modo=='target'):

            #print('target1')

            target(self,rival)         
               
            #print('target2')
        # if(self.nombre=='IA'):   
        #     creartablero.imprimirTablero(self.tableroBusqueda)
       