import chess
import chess.polyglot
import random
import engine

board = chess.Board()
#board = chess.Board('q1r4k/6pp/8/6N1/8/1Q6/6PP/7K w - - 0 1')
#board = chess.Board('5k2/8/4K3/8/8/8/2R5/8 w - - 0 1')
#board = chess.Board('5q2/8/8/8/8/6k1/8/7K w - - 0 1')


def main():

    # board = chess.Board('rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1')
    # print(board)
    # with chess.polyglot.open_reader("./DCbook_large.bin") as reader:
    #     print(random.choice(list(reader.find_all(board))).move)
    #     print("soaiodpaiaspodisapoidopasidpoaip\n")
    #
    #     for entry in reader.find_all(board):
    #         print(entry.move)

    # board.push_san("e4")
    # board.push_san("e5")
    # board.push_san("Qh5")
    # board.push_san("g6") # blunder

    while True:
        print(board)
        print('\n ------------------ \n')

        if board.is_game_over():
            print('koniec gry :)')
            print(board.result())
            break

        human_move = input('proszę podaj ruch \n')
        board.push_san(human_move)

        #move = engine.make_a_move(board, 4, True)
        #board.push(move)


        print(board)
        print('\n ------------------ \n')

        if board.is_game_over():
            print('koniec gry :)')
            print(board.result())
            break

        #human_move = input('proszę podaj ruch \n')
        move = engine.make_a_move(board, 4, False)
        board.push(move)


if __name__ == "__main__":
    main()





