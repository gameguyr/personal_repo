#!/usr/bin/python
########################
# TITLE: game_of_life
# AUTHOR: russell lego
# DATE: 2018-12-14
# PURPOSE:Your task is to write a program to calculate the next generation of Conway's game of life, given any starting position. You start with a two dimensional grid of cells, where each cell is either alive or dead. The grid is finite, and no life can exist off the edges. When calculating the next generation of the grid, follow these four rules:
#
# Any live cell with fewer than two live neighbors dies, as if caused by underpopulation.
# Any live cell with more than three live neighbors dies, as if by overcrowding.
# Any live cell with two or three live neighbors lives on to the next generation.
# Any dead cell with exactly three live neighbors becomes a live cell.
# Examples: * indicates live cell, . indicates dead cell
#
# Example input: (4 x 8 grid)
# 4 8
# ........
# ....*...
# ...**...
# ........
# Example output:
# 4 8
# ........
# ...**...
# ...**...
# ........
########################


#################################
# Importing Modules
#################################
import numpy

#################################
# Defining Constants
#################################


#################################
# Defining Functions
#################################


#################################
# Defining Classes
#################################


class GameOfLife(object):

    def __init__(self, num_rows, num_cols):
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.world_matrix = numpy.chararray((self.num_rows, self.num_cols))

        self.live = 'X'
        self.dead = 'O'
        self.world_matrix[:] = self.dead

    def reset_all_cells(self):
        self.world_matrix[:] = self.dead

    def set_cell_to_live(self, row_position, col_position):
        self.world_matrix[row_position][col_position] = self.live

    def set_cell_to_dead(self, row_position, col_position):
        self.world_matrix[row_position][col_position] = self.dead

    def is_cell_live(self, row_position, col_position):
        try:
            is_alive = self.world_matrix[row_position][col_position] == self.live
        except IndexError:
            return False

        if is_alive :
            return True
        else:
            return False

    def next_generation(self):
        index_of_live_cells = numpy.where(self.world_matrix == self.live)
        for i in range(0, len(index_of_live_cells[0])):
            # neighbors = index_of_live_cells[0]
            row_position_of_current_live_cell = index_of_live_cells[0][i]
            col_position_of_current_live_cell = index_of_live_cells[1][i]

            neighbors = [[row_position_of_current_live_cell - 1, col_position_of_current_live_cell - 1],
                         [row_position_of_current_live_cell - 1, col_position_of_current_live_cell],
                         [row_position_of_current_live_cell - 1, col_position_of_current_live_cell + 1],
                         [row_position_of_current_live_cell, col_position_of_current_live_cell - 1],
                         [row_position_of_current_live_cell + 1, col_position_of_current_live_cell - 1],
                         [row_position_of_current_live_cell + 1, col_position_of_current_live_cell],
                         [row_position_of_current_live_cell, col_position_of_current_live_cell + 1],
                         [row_position_of_current_live_cell + 1, col_position_of_current_live_cell + 1]]

            number_of_alive_neighbors = 0
            number_of_dead_neighbors = 0

            for j in range(0, len(neighbors)):
                if self.is_cell_live(neighbors[j][0], neighbors[j][1]):
                    number_of_alive_neighbors = number_of_alive_neighbors + 1
                else:
                    number_of_dead_neighbors = number_of_dead_neighbors + 1

            if number_of_alive_neighbors < 2:
                self.set_cell_to_dead(row_position_of_current_live_cell, col_position_of_current_live_cell)
            elif number_of_alive_neighbors > 3:
                self.set_cell_to_dead(row_position_of_current_live_cell, col_position_of_current_live_cell)
            elif number_of_alive_neighbors == 2 or number_of_alive_neighbors == 3:
                self.set_cell_to_live(row_position_of_current_live_cell, col_position_of_current_live_cell)

        #now checking dead cells
        index_of_dead_cells = numpy.where(self.world_matrix == self.dead)

        for i in range(0, len(index_of_dead_cells[0])):
            row_position_of_current_dead_cell = index_of_dead_cells[0][i]
            col_position_of_current_dead_cell = index_of_dead_cells[1][i]

            neighbors = [[row_position_of_current_dead_cell - 1, col_position_of_current_dead_cell - 1],
                         [row_position_of_current_dead_cell - 1, col_position_of_current_dead_cell],
                         [row_position_of_current_dead_cell - 1, col_position_of_current_dead_cell + 1],
                         [row_position_of_current_dead_cell, col_position_of_current_dead_cell - 1],
                         [row_position_of_current_dead_cell + 1, col_position_of_current_dead_cell - 1],
                         [row_position_of_current_dead_cell + 1, col_position_of_current_dead_cell],
                         [row_position_of_current_dead_cell, col_position_of_current_dead_cell + 1],
                         [row_position_of_current_dead_cell + 1, col_position_of_current_dead_cell + 1]]

            number_of_alive_neighbors = 0
            number_of_dead_neighbors = 0

            for j in range(0, len(neighbors)):
                if self.is_cell_live(neighbors[j][0], neighbors[j][1]):
                    number_of_alive_neighbors = number_of_alive_neighbors + 1
                else:
                    number_of_dead_neighbors = number_of_dead_neighbors + 1

            if number_of_alive_neighbors == 3:
                self.set_cell_to_live(row_position_of_current_dead_cell, col_position_of_current_dead_cell)


