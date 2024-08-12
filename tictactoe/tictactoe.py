"""
Tic Tac Toe Player
"""

import math
import copy 
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


def player(board: list[list]) -> str:
    """
    Returns player who has the next turn on a board.
    """
    movesMade = 0
    for row in board:
        for tile in row:
            if tile is not None:
                movesMade += 1
    return "X" if movesMade % 2 == 0 else "O"


def actions(board: list[list]):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actionSet = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                actionSet.add((i, j))
    return actionSet


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    result = copy.deepcopy(board)
    result[action[0]][action[1]] = player(board)
    return result


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # check diagonals
    piece = board[0][0]
    if piece is not None and board[1][1] == piece and board[2][2] == piece:
        return piece
    piece = board[0][2]
    if piece is not None and board[1][1] == piece and board[2][0] == piece:
        return piece

    # check verticals and horizontals
    for n in range(3):
        piece = board[0][n]
        if piece is not None and board[1][n] == piece and board[2][n] == piece:
            return piece

        piece = board[n][0]
        if piece is not None and board[n][1] == piece and board[n][2] == piece:
            return piece

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board): 
        return True
    
    for row in board:
        for cell in row:
            if cell is None:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    w = winner(board)
    if w == "X":
        return 1
    elif w == "O":
        return -1
    return 0





def max_value(board):
    if terminal(board):
        return utility(board),None
    maxeval =  float('-inf')
    res_act = None
    for action in actions(board):
        mv,act = min_value(result(board,action))
        if mv > maxeval:
            maxeval = mv
            res_act = action


    return maxeval,res_act


def min_value(board):
    if terminal(board):
        return utility(board),None
    mineval = float('inf')
    res_act = None
    for action in actions(board):
        mv,act = max_value(result(board,action))
        if mv < mineval:
            mineval = mv
            res_act = action
    return mineval,res_act

def minimax(board):
    """
    X is maximizing! 
    """
    if terminal(board):
        return None
    
    if player(board) == "X":
        mv,act= max_value(board)
        return act
    else:
        mv,act= min_value(board)
        return act
