import random, numpy
from main import board


def make_a_move(board):
    lst = list(board.legal_moves)
    return random.choice(lst)


def evaluate():
    # todo here we need fucntion that returns float value (<0 black >0 white)
    pass

class Heuristics:

    # The tables denote the points scored for the position of the chess pieces on the board.
    PAWN_TABLE = numpy.array([
        [ 0,  0,  0,  0,  0,  0,  0,  0],
        [ 5, 10, 10,-20,-20, 10, 10,  5],
        [ 5, -5,-10,  0,  0,-10, -5,  5],
        [ 0,  0,  0, 20, 20,  0,  0,  0],
        [ 5,  5, 10, 25, 25, 10,  5,  5],
        [10, 10, 20, 30, 30, 20, 10, 10],
        [50, 50, 50, 50, 50, 50, 50, 50],
        [ 0,  0,  0,  0,  0,  0,  0,  0]
    ])

    KNIGHT_TABLE = numpy.array([
        [-50, -40, -30, -30, -30, -30, -40, -50],
        [-40, -20,   0,   5,   5,   0, -20, -40],
        [-30,   5,  10,  15,  15,  10,   5, -30],
        [-30,   0,  15,  20,  20,  15,   0, -30],
        [-30,   5,  15,  20,  20,  15,   0, -30],
        [-30,   0,  10,  15,  15,  10,   0, -30],
        [-40, -20,   0,   0,   0,   0, -20, -40],
        [-50, -40, -30, -30, -30, -30, -40, -50]
    ])

    BISHOP_TABLE = numpy.array([
        [-20, -10, -10, -10, -10, -10, -10, -20],
        [-10,   5,   0,   0,   0,   0,   5, -10],
        [-10,  10,  10,  10,  10,  10,  10, -10],
        [-10,   0,  10,  10,  10,  10,   0, -10],
        [-10,   5,   5,  10,  10,   5,   5, -10],
        [-10,   0,   5,  10,  10,   5,   0, -10],
        [-10,   0,   0,   0,   0,   0,   0, -10],
        [-20, -10, -10, -10, -10, -10, -10, -20]
    ])

    ROOK_TABLE = numpy.array([
        [ 0,  0,  0,  5,  5,  0,  0,  0],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [-5,  0,  0,  0,  0,  0,  0, -5],
        [ 5, 10, 10, 10, 10, 10, 10,  5],
        [ 0,  0,  0,  0,  0,  0,  0,  0]
    ])

    QUEEN_TABLE = numpy.array([
        [-20, -10, -10, -5, -5, -10, -10, -20],
        [-10,   0,   5,  0,  0,   0,   0, -10],
        [-10,   5,   5,  5,  5,   5,   0, -10],
        [  0,   0,   5,  5,  5,   5,   0,  -5],
        [ -5,   0,   5,  5,  5,   5,   0,  -5],
        [-10,   0,   5,  5,  5,   5,   0, -10],
        [-10,   0,   0,  0,  0,   0,   0, -10],
        [-20, -10, -10, -5, -5, -10, -10, -20]
    ])

class AI:
    INFINITE = 10000000

    def minimax(board, depth, maximizing, WHITE="W", BLACK="B"):
        if (depth == 0):
            return Heuristics.evaluate(board)

        if (maximizing):
            best_score = -AI.INFINITE
            for move in board.get_possible_moves(WHITE):
                copy = board.Board.clone(board)
                copy.perform_move(move)

                score = AI.minimax(copy, depth-1, False)
                best_score = max(best_score, score)

            return best_score
        else:
            best_score = AI.INFINITE
            for move in board.get_possible_moves(BLACK):
                copy = board.Board.clone(board)
                copy.perform_move(move)

                score = AI.minimax(copy, depth-1, True)
                best_score = min(best_score, score)

            return best_score

    def alphabeta(chessboard, depth, a, b, maximizing, WHITE="W", BLACK="B"):
        if (depth == 0):
            return Heuristics.evaluate(chessboard)

        if (maximizing):
            best_score = -AI.INFINITE
            for move in chessboard.get_possible_moves(WHITE):
                copy = board.Board.clone(chessboard)
                copy.perform_move(move)

                best_score = max(best_score, AI.alphabeta(copy, depth-1, a, b, False))
                a = max(a, best_score)
                if (b <= a):
                    break
            return best_score
        else:
            best_score = AI.INFINITE
            for move in chessboard.get_possible_moves(BLACK):
                copy = board.Board.clone(chessboard)
                copy.perform_move(move)

                best_score = min(best_score, AI.alphabeta(copy, depth-1, a, b, True))
                b = min(b, best_score)
                if (b <= a):
                    break
            return best_score