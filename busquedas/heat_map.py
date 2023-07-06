import numpy as np
import random
import creartablero


def gen_prob_map(self):
    SHIPS = {"Portaaviones": 5, "Acorazado": 4,
             "Destructor": 3, "Submarino": 3, "Bote": 2}
    prob_map = np.zeros([10, 10])
    for ship_name in set(SHIPS.keys()):
        ship_size = SHIPS[ship_name]
        use_size = ship_size - 1
        for row in range(10):
            for col in range(10):
                if self.tableroBusqueda[row][col] != 'X' and self.tableroBusqueda[row][col] != 'E':
                    # get potential ship endpoints
                    endpoints = []
                    # add 1 to all endpoints to compensate for python indexing
                    if row - use_size >= 0:
                        endpoints.append(
                            ((row - use_size, col), (row + 1, col + 1)))
                    if row + use_size <= 9:
                        endpoints.append(
                            ((row, col), (row + use_size + 1, col + 1)))
                    if col - use_size >= 0:
                        endpoints.append(
                            ((row, col - use_size), (row + 1, col + 1)))
                    if col + use_size <= 9:
                        endpoints.append(
                            ((row, col), (row + 1, col + use_size + 1)))

                    for (start_row, start_col), (end_row, end_col) in endpoints:
                        are_all_ceros = True
                        for sub_row in range(start_row, end_row):
                            for sub_col in range(start_col, end_col):
                                if (self.tableroBusqueda[sub_row][sub_col] != 0):
                                    are_all_ceros = False
                        if are_all_ceros:
                            prob_map[start_row:end_row, start_col:end_col] += 1
                if self.tableroBusqueda[row][col] == 'X':

                    if (row + 1 <= 9) and (self.tableroBusqueda[row + 1][col] == 0):
                        prob_map[row + 1][col] += 13
                    if (row - 1 >= 0) and (self.tableroBusqueda[row - 1][col] == 0):
                        prob_map[row - 1][col] += 13
                    if (col + 1 <= 9) and (self.tableroBusqueda[row][col + 1] == 0):
                        prob_map[row][col + 1] += 13
                    if (col - 1 >= 0) and (self.tableroBusqueda[row][col - 1] == 0):
                        prob_map[row][col - 1] += 13
                elif self.tableroBusqueda[row][col] == 'E':
                    prob_map[row][col] = 0
                    if (row + 1 <= 9) and (self.tableroBusqueda[row + 1][col] == 0):
                        prob_map[row + 1][col] -= 5
                        if (prob_map[row + 1][col] <= 4):
                            prob_map[row + 1][col] = 5
                    if (row - 1 >= 0) and (self.tableroBusqueda[row - 1][col] == 0):
                        prob_map[row - 1][col] -= 5
                        if (prob_map[row - 1][col] <= 4):
                            prob_map[row - 1][col] = 5
                    if (col + 1 <= 9) and (self.tableroBusqueda[row][col + 1] == 0):
                        prob_map[row][col + 1] -= 5
                        if (prob_map[row][col + 1] <= 4):
                            prob_map[row][col + 1] = 5
                    if (col - 1 >= 0) and (self.tableroBusqueda[row][col - 1] == 0):
                        prob_map[row][col - 1] -= 5
                        if (prob_map[row][col - 1] <= 4):
                            prob_map[row][col - 1] = 5
                if self.tableroBusqueda[row][col] == 0:
                    prob_map[row][col] += .5
    self.PROB_MAP = prob_map


def guess_prob(self):
    self.gen_prob()
    # get the row, col numbers of the largest element in PROB_MAP
    # https://thispointer.com/find-max-value-its-index-in-numpy-array-numpy-amax/
    max_indices = np.where(self.PROB_MAP == np.amax(self.PROB_MAP))
    guess_row, guess_col = max_indices[0][0], max_indices[1][0]

    return guess_row, guess_col


def busqueda_heat_map(self, rival):
    flag = False
    while not flag:
        guess_row, guess_col = guess_prob(self)
        if (self.pregunta(rival, guess_row, guess_col)):
            self.tableroBusqueda[guess_row][guess_col] = 'X'
            creartablero.imprimirTablero(self.tableroBusqueda)
            creartablero.imprimirTablero(self.PROB_MAP)
        else:
            self.tableroBusqueda[guess_row][guess_col] = 'E'
        flag = self.flota_rival_hundida()

    return 0
