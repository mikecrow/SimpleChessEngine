import chess
import engine

board = chess.Board('7k/7p/P7/4K3/8/8/8/8 w - - 0 1')
#board = chess.Board('r1b1k2r/p1qpbppp/npp1p2n/8/2BPP3/2N1BN2/PPP2PPP/R2Q1RK1 w kq - 2 8')
#board = chess.Board('q1r4k/6pp/8/6N1/8/1Q6/6PP/7K w - - 0 1')
#board = chess.Board('5k2/8/4K3/8/8/8/2R5/8 w - - 0 1')
#board = chess.Board('5q2/8/8/8/8/6k1/8/7K w - - 0 1')


def main():

    a = engine.evaluate(board)
    print(a)
    print(engine.check_end_game(board))
    print(board)
    print(engine.make_a_move(board, 6, True))

    while True:
        print(board)
        print('\n ------------------ \n')

        if board.is_game_over():
            print('koniec gry :)')
            print(board.result())
            break

        # human_move = input('proszę podaj ruch \n')
        # board.push_san(human_move)

        move = engine.make_a_move(board, 5, True)
        board.push(move)

        print(board)
        print('\n ------------------ \n')

        if board.is_game_over():
            print('koniec gry :)')
            print(board.result())
            break

        move = engine.make_a_move(board, 1, False)
        board.push(move)


if __name__ == "__main__":
    main()





