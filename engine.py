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

pawn_white = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0,
]

pawn_black = [
    0, 0, 0, 0, 0, 0, 0, 0,
    50, 50, 50, 50, 50, 50, 50, 50,
    10, 10, 20, 30, 30, 20, 10, 10,
    5, 5, 10, 25, 25, 10, 5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, -5, -10, 0, 0, -10, -5, 5,
    5, 10, 10, -20, -20, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0,
]

knight_white = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50,
]

knight_black = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50,
]

bishop_white = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20,
]


bishop_black = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -20, -10, -10, -10, -10, -10, -10, -20,
]

rook_white = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0,
]

rook_black = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, 10, 10, 10, 10, 5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    0, 0, 0, 5, 5, 0, 0, 0,
]
queen_white = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -10, 5, 5, 5, 5, 5, 0, -10,
    0, 0, 5, 5, 5, 5, 0, -5,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20,
]

queen_black = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -5, 0, 5, 5, 5, 5, 0, -5,
    0, 0, 5, 5, 5, 5, 0, -5,
    -10, 5, 5, 5, 5, 5, 0, -10,
    -10, 0, 5, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20,
]

king_white = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
]

king_black = [
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    20, 20, 0, 0, 0, 0, 20, 20,
    20, 30, 10, 0, 0, 10, 30, 20,
]

king_white_endgame = [
    -50, -30, -30, -30, -30, -30, -30, -50,
    -30, -30, 0, 0, 0, 0, -30, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -20, -10, 0, 0, -10, -20, -30,
    -50, -40, -30, -20, -20, -30, -40, -50,
]

king_black_endgame = [
    -50, -40, -30, -20, -20, -30, -40, -50,
    -30, -20, -10, 0, 0, -10, -20, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 30, 40, 40, 30, -10, -30,
    -30, -10, 20, 30, 30, 20, -10, -30,
    -30, -30, 0, 0, 0, 0, -30, -30,
    -50, -30, -30, -30, -30, -30, -30, -50
]


def evaluate_piece(piece, square, endgame):
    base_value = piece_values[piece.piece_type]

    if piece.piece_type == chess.PAWN:
        if piece.color == chess.WHITE:
            return base_value + pawn_white[square]
        else:
            return -(base_value + pawn_black[square])

    elif piece.piece_type == chess.ROOK:
        if piece.color == chess.WHITE:
            return base_value + rook_white[square]
        else:
            return -(base_value + rook_black[square])

    elif piece.piece_type == chess.KNIGHT:
        if piece.color == chess.WHITE:
            return base_value + knight_white[square]
        else:
            return -(base_value + knight_black[square])

    elif piece.piece_type == chess.BISHOP:
        if piece.color == chess.WHITE:
            return base_value + bishop_white[square]
        else:
            return -(base_value + bishop_black[square])

    elif piece.piece_type == chess.QUEEN:
        if piece.color == chess.WHITE:
            return base_value + queen_white[square]
        else:
            return -(base_value + queen_black[square])

    else:
        if not endgame:
            if piece.color == chess.WHITE:
                return base_value + king_white[square]
            else:
                return -(base_value + king_black[square])
        else:
            if piece.color == chess.WHITE:
                return base_value + king_white_endgame[square]
            else:
                return -(base_value + king_black_endgame[square])


def check_end_game(board):
    white_queens = 0
    white_rooks = 0
    white_minor_pieces = 0
    black_queens = 0
    black_rooks = 0
    black_minor_pieces = 0

    white_endgame = False
    black_endgame = False

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if piece and piece.piece_type == chess.QUEEN:
            if piece.color == chess.WHITE:
                white_queens += 1
            else:
                black_queens += 1
        if piece and piece.piece_type == chess.QUEEN:
            if piece.color == chess.WHITE:
                white_rooks += 1
            else:
                black_rooks += 1
        if piece and (piece.piece_type == chess.BISHOP or piece.piece_type == chess.KNIGHT):
            if piece.color == chess.WHITE:
                white_minor_pieces += 1
            else:
                black_minor_pieces += 1

    if white_queens == 0 or (white_queens == 1 and white_rooks == 0 and white_minor_pieces <= 1):
        white_endgame = True
    if black_queens == 0 or (black_queens == 1 and black_rooks == 0 and black_minor_pieces <= 1):
        black_endgame = True

    return white_endgame and black_endgame


def evaluate(board):
    end_game = check_end_game(board)
    value = 0

    for square in chess.SQUARES:
        piece = board.piece_at(square)
        if not piece:
            continue

        value += evaluate_piece(piece, square, end_game)

    return value


def minimax(board, depth, alpha, beta, maximizing_player, moves):
    if board.is_game_over():
        if board.result() == '1-0':
            return 100000 - moves
        elif board.result() == '0-1':
            return -100000 + moves
        elif board.result() == '1/2-1/2':
            return 0

    if depth == 0:
        return evaluate(board)

    if maximizing_player:
        value = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            value = max(value, minimax(board, alpha, beta, depth - 1, False, moves + 1))
            board.pop()
            if beta <= alpha:
                return value
        return value
    else:
        value = float('inf')
        for move in board.legal_moves:
            board.push(move)
            value = min(value, minimax(board, alpha, beta, depth - 1, True, moves + 1))
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
                print(move, value)

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
                print(move, value)

        return best_move
