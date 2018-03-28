"""This file is provided as a starting template for writing your own unit
tests to run and debug your minimax and alphabeta agents locally.  The test
cases used by the project assistant are not public.
"""

import unittest

import isolation
import game_agent
from sample_players import *

from importlib import reload


class IsolationTest(unittest.TestCase):
    """Unit tests for isolation agents"""

    def setUp(self):
        reload(game_agent)
        self.player1 = game_agent.AlphaBetaPlayer()
        # self.player2 = game_agent.MinimaxPlayer()
        self.player2 = GreedyPlayer()
        # self.player1 = "Player1"
        # self.player2 = "Player2"
        self.game = isolation.Board(self.player1, self.player2)
        self.game.apply_move((2, 3))
        self.game.apply_move((0, 5))
        print(self.game.to_string())

    def test(self):

        winner, history, outcome = self.game.play()
        print("\nWinner: {}\nOutcome: {}".format(winner, outcome))
        print(self.game.to_string())
        print("Move history:\n{!s}".format(history))

        # self.assertTrue("move" == "illegalmove")


if __name__ == '__main__':
    unittest.main()
