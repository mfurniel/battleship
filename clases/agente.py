from clases import barco 
import creartablero
from busquedas.greedy import busqueda_greedy 
from busquedas.greedy_hunt import busqueda_greedy_hunt
from busquedas.aleatorio import busqueda_aleatoria


class Agente:
    def __init__(self):
        self.tablerobBusqueda = [[0] * 10 for _ in range(10)]
        self.tableroPropio = creartablero.generar_tablero(10, 10)
        self.memoria = []
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
        count_x = sum(row.count('X') for row in self.tablerobBusqueda)
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

    
    #LA idea seria agregar aqui las busquedas

    def greedy(self,rival):
        busqueda_greedy(self,rival)
    
    def greedy_hunt(self):
        busqueda_greedy_hunt(self)

    def aleatorio(self,rival):
        busqueda_aleatoria(self,rival)

    def cambiar_tablero_propio(self,tablero):
        self.tableroPropio=tablero
    

