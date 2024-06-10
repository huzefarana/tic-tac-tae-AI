import unittest
 
from tictactoe import initial_state, player, X, O, actions
from tictactoe import EMPTY as _, result, winner, terminal, utility, min_value, max_value, minimax

class TestTicTacToe(unittest.TestCase):
    def test_initial_state(self):
        board = initial_state()
        self.assertEqual(board, [[_, _, _], [_, _, _], [_, _, _]])
 
    def test_player(self):
        board = initial_state()
        self.assertEqual(player(board), X)
        board = result(board, (0, 0))
        self.assertEqual(player(board), O)
 
    def test_actions(self):
        board = initial_state()
        expected_actions = {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
        self.assertEqual(set(actions(board)), expected_actions)

        board = result(board, (0, 0))
        expected_actions = {(0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)}
        self.assertEqual(set(actions(board)), expected_actions)

    
    def test_result(self):
        board = initial_state()
        new_board = result(board, (0, 0))
        self.assertEqual(new_board, [[X, _, _], [_, _, _], [_, _, _]])
        new_board = result(new_board, (1, 1))
        self.assertEqual(new_board, [[X, _, _], [_, O, _], [_, _, _]])
 
    def test_winner(self):
        board = [[X, O, X], [O, X, O], [X, O, X]]
        self.assertEqual(winner(board), None)
        board = [[X, O, X], [O, X, O], [X, O, O]]
        self.assertEqual(winner(board), O)
        board = [[X, O, X], [O, X, O], [X, X, O]]
        self.assertEqual(winner(board), X)
 
    def test_terminal(self):
        board = [[X, O, X], [O, X, O], [X, O, X]]
        self.assertEqual(terminal(board), True)
        board = [[X, O, X], [O, X, O], [X, _, _]]
        self.assertEqual(terminal(board), False)
 
    def test_utility(self):
        board = [[X, O, X], [O, X, O], [X, O, X]]
        self.assertEqual(utility(board), 0)
        board = [[X, O, X], [O, X, O], [X, O, O]]
        self.assertEqual(utility(board), -1)
        board = [[X, O, X], [O, X, O], [X, X, O]]
        self.assertEqual(utility(board), 1)
    
    def test_minimax(self):
        board = [[X, O, X], [O, X, O], [X, _, _]]
        self.assertEqual(minimax(board), (2, 1))
        board = [[X, O, X], [O, X, O], [X, O, _]]
        self.assertEqual(minimax(board), (2, 2))
        board = [[X, O, X], [O, X, O], [X, X, O]]
        self.assertEqual(minimax(board), (2, 2))

    def test_min_value_terminal(self):
        board = [[X, O, X], [O, X, O], [X, O, X]]
        self.assertEqual(min_value(board), utility(board))

    def test_min_value_non_terminal(self):
        board = [[X, O, X], [O, _, O], [X, O, X]]
        expected_value = 1
        self.assertEqual(min_value(board), expected_value)

    def test_max_value_terminal(self):
        board = [[X, O, X], [O, X, O], [X, O, X]]
        self.assertEqual(max_value(board), utility(board))

    def test_max_value_non_terminal(self):
        board = [[X, O, X], [O, _, O], [X, O, X]]
        expected_value = 1
        self.assertEqual(max_value(board), expected_value)
    
if __name__ == '__main__':
    unittest.main()