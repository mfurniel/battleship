import barco
from busquedas.greedy import busqueda_greedy 
from busquedas.greedy_hunt import busqueda_greedy_hunt

class Agente:
    def __init__(self):
        self.tablero = [[0] * 10 for _ in range(10)]
        self.memoria = []
        self.agregar_barcos_predeterminados()

    def agregar_barcos_predeterminados(self):
        barcos = [
            barco.Barco("Portaaviones", 5),
            barco.Barco("Acorazado", 4),
            barco.Barco("Destructor", 3),
            barco.Barco("Submarino", 3),
            barco.Barco("Bote", 2)
        ]
        self.memoria.extend(barcos)

    #LA idea seria agregar aqui las busquedas
    def greedy(self):
        busqueda_greedy(self)
    
    def greedy_hunt(self):
        busqueda_greedy_hunt(self)

    
    

