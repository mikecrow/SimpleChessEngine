import chess
import engine

board = chess.Board()


def main():

    # board.push_san("e4")
    # board.push_san("e5")
    # board.push_san("Qh5")
    # board.push_san("g6") # blunder

    while not board.is_game_over():
        print(board)
        move = engine.choose_move(board, 3)
        board.push(move)


if __name__ == "__main__":
    main()





