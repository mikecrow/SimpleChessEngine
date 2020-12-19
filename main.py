import chess
import engine
import chess.svg
from PyQt5.QtSvg import QSvgWidget
from PyQt5.QtWidgets import QApplication, QWidget

board = chess.Board()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.widgetSvg = QSvgWidget(parent=self)
        self.widgetSvg.setGeometry(10, 10, 800, 800)

        self.chessboard = board

    def paintEvent(self, event):
        self.chessboardSvg = chess.svg.board(self.chessboard).encode("UTF-8")
        self.widgetSvg.load(self.chessboardSvg)
    pass

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()



    # def test():
    #     if board.is_game_over():
    #         print(board)
    #         move1 = input("make a move please:\n")
    #         board.push_san(move1)
    #
    #         move2 = engine.make_a_move(board)
    #         board.push(move2)
    #     pass
    # todo import chess api and make random moves




