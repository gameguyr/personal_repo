#!/usr/bin/python
########################
# TITLE: game_of_life_test
# AUTHOR: russell lego
# DATE: 2018-12-14
# PURPOSE:
########################
import unittest
from game_of_life import GameOfLife

class GameOfLifeTest(unittest.TestCase):
    def __init__(self, args, *kwargs):
        super(GameOfLifeTest, self).__init__(args, *kwargs)
        self.game_of_life_class = GameOfLife(6, 8)


    def test_any_live_cell_with_fewer_than_two_neighbors_dies(self):
        self.game_of_life_class.reset_all_cells()
        self.game_of_life_class.set_cell_to_live(1, 3)
        self.game_of_life_class.set_cell_to_live(3, 2)
        self.game_of_life_class.set_cell_to_live(3, 3)
        self.game_of_life_class.set_cell_to_live(3, 4)
        self.game_of_life_class.set_cell_to_live(2, 4)
        # now the game is set up

        self.game_of_life_class.next_generation()

        self.assertFalse(self.game_of_life_class.is_cell_live(1, 3))

    def test_any_live_cell_with_more_than_3_live_neighbors_dies(self):
        self.game_of_life_class.reset_all_cells()
        self.game_of_life_class.set_cell_to_live(2, 3)
        self.game_of_life_class.set_cell_to_live(3, 3)
        self.game_of_life_class.set_cell_to_live(2, 4)
        self.game_of_life_class.set_cell_to_live(3, 4)
        self.game_of_life_class.set_cell_to_live(4, 3)
        # now the game is set up

        self.game_of_life_class.next_generation()

        self.assertFalse(self.game_of_life_class.is_cell_live(3, 3))

    def test_any_live_cell_with_2_or_3_neighbors_lives(self):
        self.game_of_life_class.reset_all_cells()
        self.game_of_life_class.set_cell_to_live(2, 2)
        self.game_of_life_class.set_cell_to_live(2, 4)
        self.game_of_life_class.set_cell_to_live(3, 3)
        self.game_of_life_class.set_cell_to_live(3, 4)
        self.game_of_life_class.set_cell_to_live(4, 3)
        # now the game is set up

        self.game_of_life_class.next_generation()

        self.assertTrue(self.game_of_life_class.is_cell_live(2, 4))

    def test_any_dead_cell_with_exactly_3_neighbors_becomes_live_cell(self):
        self.game_of_life_class.reset_all_cells()
        self.game_of_life_class.set_cell_to_live(2, 2)
        self.game_of_life_class.set_cell_to_live(2, 4)
        self.game_of_life_class.set_cell_to_live(3, 3)
        self.game_of_life_class.set_cell_to_live(3, 4)
        self.game_of_life_class.set_cell_to_live(4, 3)
        # now the game is set up

        self.game_of_life_class.next_generation()

        self.assertTrue(self.game_of_life_class.is_cell_live(4, 4))
