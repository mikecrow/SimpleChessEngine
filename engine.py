import chess

piece_values = {
    chess.PAWN: 100,
    chess.ROOK: 500,
    chess.KNIGHT: 320,
    chess.BISHOP: 330,
    chess.QUEEN: 900,
    chess.KING: 20000
}


def evaluate(board):
    if board.result() == '1-0':
        return float('inf')
    elif board.result() == '0-1':
        return -float('inf')

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


def minimax(board, depth, maximizing_player):
    if depth == 0 or board.is_game_over():
        return evaluate(board)
    if maximizing_player:
        value = -float('inf')
        for move in board.legal_moves:
            board.push(move)
            value = max(value, minimax(board, depth - 1, False))
            board.pop()
        return value
    else:
        value = float('inf')
        for move in board.legal_moves:
            board.push(move)
            value = min(value, minimax(board, depth - 1, True))
            board.pop()
        return value
    # TODO alpha beta


def choose_move(board, depth):
    value = -float('inf')
    best_move = None
    for move in board.legal_moves:
        board.push(move)
        new_value = minimax(board, depth, False)
        board.pop()
        if new_value > value:
            best_move = move
            value = new_value

    return best_move
