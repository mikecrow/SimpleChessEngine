import random

def make_a_move(board):
    lst = list(board.legal_moves)
    return random.choice(lst)


def evaluate():
    # todo here we need fucntion that returns float value (<0 black >0 white)
    pass