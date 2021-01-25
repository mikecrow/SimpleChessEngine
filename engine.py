import chess
import chess.polyglot

piece_values = {
    chess.PAWN: 100,
    chess.ROOK: 500,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.QUEEN: 900,
    chess.KING: 20000
}


def evaluate(board):

    white_material = 0
    black_material = 0
    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if not piece:
            continue
        if piece.color == chess.WHITE:
            white_material += piece_values[piece.piece_type]
        else:
            black_material += piece_values[piece.piece_type]
    return white_material - black_material
    # TODO better eval


def minimax(board, depth, alpha, beta, maximizing_player, moves):
    if board.is_game_over():
        if board.result() == '1-0':
            return 100000-moves
        elif board.result() == '0-1':
            return -100000+moves
        elif board.result() == '1/2-1/2':
            return 0

    if depth == 0:
        return evaluate(board)

    if maximizing_player:
        value = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            value = max(value, minimax(board, alpha, beta, depth - 1, False, moves+1))
            board.pop()
            if beta <= alpha:
                return value
        return value
    else:
        value = float('inf')
        for move in board.legal_moves:
            board.push(move)
            value = min(value, minimax(board, alpha, beta, depth - 1, True, moves+1))
            board.pop()
            if beta <= alpha:
                return value
        return value


def make_a_move(board, depth, maximizing_player):

    with chess.polyglot.open_reader("./DCbook_large.bin") as reader:
        try:
            book_move = reader.weighted_choice(board).move
            return book_move
        except IndexError:
            pass

    if maximizing_player:
        value = -float('inf')
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            new_value = minimax(board, depth - 1, -float('inf'), float('inf'), False, 1)
            board.pop()
            if new_value >= value:
                best_move = move
                value = new_value
                # print(move, value)

        return best_move
    else:
        value = float('inf')
        best_move = None
        for move in board.legal_moves:
            board.push(move)
            new_value = minimax(board, depth - 1, -float('inf'), float('inf'), True, 1)
            board.pop()
            if new_value <= value:
                best_move = move
                value = new_value
                # print(move, value)

        return best_move

