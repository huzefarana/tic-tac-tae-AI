"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """ 
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return X
    if terminal(board):
        return None
    else:
        x_count = 0
        o_count = 0
        for row in board:
            for cell in row:
                if cell == X:
                    x_count += 1
                elif cell == O:
                    o_count += 1
        if x_count > o_count:
            return O
        else:
            return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                actions.add((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = [[cell for cell in row] for row in board]
    i, j = action
    if new_board[i][j] != EMPTY:
        raise Exception("Invalid move")
    new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    f# Row checking
    for row in board:
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O

    # Column checking
    for col in range(len(board[0])):
        if board[0][col] == X and board[1][col] == X and board[2][col] == X:
            return X
        if board[0][col] == O and board[1][col] == O and board[2][col] == O:
            return O

    # Diagonal checking
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O

    # Anti-Diagonal checking
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    for row in board:
        for cell in row:
            if cell == EMPTY:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    if player(board) == X:
        v = -math.inf
        for action in actions(board):
            new_v = min_value(result(board, action))
            if new_v > v:
                v = new_v
                optimal_action = action
    else:
        v = math.inf
        for action in actions(board):
            new_v = max_value(result(board, action))
            if new_v < v:
                v = new_v
                optimal_action = action
    return optimal_action

def min_value(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v

def max_value(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

