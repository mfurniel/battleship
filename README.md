
# BatleSheap

Este es un juego de batalla naval donde dos jugadores compiten para hundir los barcos del oponente. El juego se juega en un tablero cuadrado de 10x10 celdas. El obejtivo de este proyecto es implementar una IA la cual pueda jugar de la manera mas eficaz posible.

## Reglas

- Tamaño del tablero: El tablero debe ser un cuadrado con un tamaño de 10x10 celdas.
- Tipos y cantidad de barcos: Cada jugador tiene los siguientes tipos y cantidad de barcos:
  - 1 portaaviones: 5 celdas de longitud
  - 1 acorazado: 4 celdas de longitud
  - 2 cruceros: 3 celdas de longitud
  - 2 destructores: 2 celdas de longitud
  - 2 submarinos: 1 celda de longitud
  Cada jugador tiene un total de 8 barcos.
- Gana el jugador que hunde todos los barcos del oponente primero.


## Enlace artículo recomendado 

Puedes encontrar más información sobre la implementación de un agente inteligente para el juego de batalla naval en el siguiente enlace: [Coding an Intelligent Battleship Agent](https://towardsdatascience.com/coding-an-intelligent-battleship-agent-bf0064a4b319)

## Terminologia:

    Tablero:

    si la casilla tiene los siguientes valores significan:
    0: no explorado, no hay nada en el Tablero Propio y Tablero de Busqueda
    1: parte de un barco, en el Tabalero Propio
    X: parte de un barco, en el Tablero de Busqueda
    E: explorada, no hay nada en el Tablero de Busqueda

## Acercadel Codigo

#