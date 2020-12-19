import chess
import engine

print("hello")

board = chess.Board()


# todo import chess api and make random moves

while not board.is_game_over():

    print(board)
    move1 = input("make a move please:\n")
    board.push_san(move1)

    move2 = engine.make_a_move(board)
    board.push(move2)










