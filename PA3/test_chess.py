# Genghe Zhu
# CS76, PA3
# Fall 2022

# pip3 install python-chess

import chess
from RandomAI import RandomAI
from HumanPlayer import HumanPlayer
from MinimaxAI import MinimaxAI
from AlphaBetaAI import AlphaBetaAI
from ChessGame import ChessGame
from IterativeDeepening import IterativeDeepening

import sys


player1 = HumanPlayer()
player2 = RandomAI()

# my own testing players
player3 = MinimaxAI(3)
player4 = MinimaxAI(2)
player5 = MinimaxAI(1)
player6 = AlphaBetaAI(3)
player7 = AlphaBetaAI(2)
player8 = AlphaBetaAI(1)
player9 = IterativeDeepening(3)

game = ChessGame(player4, player8)

# initiating a turn counter
turn = 1

while not game.is_game_over():
    print(game)
    print("turn # " + str(turn))
    game.make_move()
    turn += 1
print("************ end of game **************")
print(game)
# print(hash(str(game.board)))
#stop
# the chess puzzle posted on EdDiscussion to test minimax against human
# created a new ChessGame constructor to set up the board exactly as the puzzle
game1 = ChessGame(player1, player3)

# human move at b1c2

# initiating turn counter
turn = 1

while not game1.is_game_over():
    print(game1)
    print("turn # " + str(turn))
    game1.make_move()
    turn += 1
print("************ end of game **************")
# print end position 
print(game1) 
