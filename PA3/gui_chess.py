# Genghe Zhu
# CS76, PA3
# Fall 2022

# brew install pyqt
from PyQt5 import QtGui, QtSvg
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PyQt5.QtWidgets import QApplication, QWidget
import sys
import chess, chess.svg
from RandomAI import RandomAI
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame
from HumanPlayer import HumanPlayer

import random


class ChessGui:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

        self.game = ChessGame(player1, player2)

        self.app = QApplication(sys.argv)
        self.svgWidget = QtSvg.QSvgWidget()
        self.svgWidget.setGeometry(50, 50, 400, 400)
        self.svgWidget.show()


    def start(self):
        self.timer = QTimer()
        if not self.game_over():
            self.timer.timeout.connect(self.make_move)
            self.timer.start(10)

        print("game over")

        self.display_board()

    def display_board(self):
        svgboard = chess.svg.board(self.game.board)

        svgbytes = QByteArray()
        svgbytes.append(svgboard)
        self.svgWidget.load(svgbytes)


    def make_move(self):

        print("making move, white turn " + str(self.game.board.turn))
        try:
            self.game.make_move()
            self.display_board()
        except:
            print("game over")
            self.display_board()

    def game_over(self):
        return self.game.is_game_over()



if __name__ == "__main__":

    random.seed(1)

    #player_ronda = RandomAI()

    # to do: gui does not work well with HumanPlayer, due to input() use on stdin conflict
    #   with event loop.

    player1 = RandomAI()
    player2 = RandomAI()
    player3 = MinimaxAI(1)
    player4 = MinimaxAI(2)
    player5 = MinimaxAI(3)
    player6 = AlphaBetaAI(1)
    player7 = AlphaBetaAI(2)
    player8 = AlphaBetaAI(4)


    game = ChessGame(player3, player4)
    gui = ChessGui(player3, player4)

    gui.start()

    sys.exit(gui.app.exec_())
