# Genghe Zhu
# CS76, PA3
# Fall 2022

import chess
import math
from math import inf
import random

class AlphaBetaAI():
    # constructor
    def __init__(self, depth):
        self.depth = depth
        self.turn = None
        self.visited = 0

    # choose best move
    def choose_move(self, board):
        self.turn = board.turn
        self.visited = 0

        chosen_move = None
        best_value = -1*math.inf
        # shuffle board moves so that you don't do the same move every time for shallow depths 
        moves = random_shuffle(board.legal_moves)
        # loop through moves and call minimax
        for move in list(moves):
            board.push(move)
            value = self.minimax(board, self.depth - 1, False, -math.inf, math.inf)
            board.pop()

            if value > best_value:
                best_value = value
                chosen_move = move

        print("Alpha Beta AI recommending move " + str(chosen_move) + " after trying " + str(self.visited) + " moves at depth = " + str(self.depth))
        return chosen_move

    # own functions, functions above are given
    def minimax(self, board, depth, max, alpha, beta):
        self.visited += 1

        if self.cutoff_test(board, depth):
            # print("Evalutaion Function: Positional")
            return self.positional_evaluation(board)
            #return self.material_evaluation(board)
        
        # maximizing turn
        if max:
            value = self.max_value(board, depth, alpha, beta)
        # minimizing turn
        else:
            value = self.min_value(board, depth, alpha, beta)
        
        return value

    # max value part of minimax
    def max_value(self, board, depth, alpha, beta):
        value = -1*math.inf
        for move in list(board.legal_moves):
            board.push(move)
            move_value = self.minimax(board, depth - 1, False, alpha, beta)
            board.pop()

            # the alpha seting part
            if move_value > value:
                value = move_value
                alpha = max(alpha, value)

            # alpha beta pruning part
            if beta <= alpha:
                break

        return value

    # mininum value part of minimax
    def min_value(self, board, depth, alpha, beta):
        value = math.inf
        # loop through successors
        for move in list(board.legal_moves):
            board.push(move)
            move_value = self.minimax(board, depth - 1, True, alpha, beta)
            board.pop()

            if move_value < value:
                value = move_value
                beta = min(beta, value)

            # alpha beta pruning
            if beta <= alpha:
                break

        return value

    # cutoff test if game over or reach depth
    def cutoff_test(self, board, depth):
        if board.is_game_over():
            return True
        if depth <= 0:
            return True
        return False

        # ceiling division function for positional_evaluation 
    def ceildiv(self, a, b):
        return -(a // -b)

    # use both piece value and position of pieces to determine evaluation function
    def positional_evaluation(self, board):
        if board.is_checkmate():
            if board.turn == self.turn:
                return -10000
            else:
                return 10000
        
        # initialize own piece total and opponent piece totals
        own_piece_tot = 0
        opp_piece_tot = 0
        pos_imp = 2 # to tune

        # loop thorugh the board
        for i in range(0, 64):
            piece = board.piece_at(i)

            if piece != None:
                # get the row by ceiling division
                row = self.ceildiv(i, 8)
                # get the column by mod
                col = i % 8
                if piece.color == self.turn:
                    # only use positional importance if the piece is not the king
                    if self.piece_value(piece) != 10000:
                        # middle pieces are better positioned (row, col) = (4,4), (4,5), (5,4), (5,5) would be the best
                        own_piece_tot += self.piece_value(piece) * (pos_imp - (0.1 * abs(row - 4.5)) - (0.1 * abs(col - 4.5)))
                    else:
                        own_piece_tot += self.piece_value(piece)
                else:
                    # only use positional importance if the piece is not the king
                    if self.piece_value(piece) != 10000:
                        # middle pieces are better positioned (row, col) = (4,4), (4,5), (5,4), (5,5) would be the best
                        opp_piece_tot += self.piece_value(piece) * (pos_imp - (0.1 * abs(row - 4.5)) - (0.1 * abs(col - 4.5)))
                    else:
                        opp_piece_tot += self.piece_value(piece)

        
        return own_piece_tot - opp_piece_tot

    # material evaluation function only takes piece count into account
    def material_evaluation(self, board):

        # check checkmate
        if board.is_checkmate():
            if board.turn == self.turn:
                return -10000
            else:
                return 10000

        # initialize own piece total and opponent piece totals
        own_piece_tot = 0
        opp_piece_tot = 0

        # loop through board
        for i in range(0, 64):
            piece = board.piece_at(i)

            # add up pieces for white and black
            if piece != None:
                if piece.color == self.turn:
                    own_piece_tot += self.piece_value(piece)
                else:
                    opp_piece_tot += self.piece_value(piece)

        # print("own piece tot: " + str(own_piece_tot))
        # print("opp piece tot: " + str(opp_piece_tot))

        return own_piece_tot - opp_piece_tot

    # piece value for evaluation functions
    def piece_value(self, piece):
        piece_name = str(piece).lower()
        # print(piece_name)
        if piece_name == "p":
            return 1
        if piece_name == "n" or piece_name == "b":
            return 3
        if piece_name == "r":
            return 5
        if piece_name == "q":
            return 9
        if piece_name == "k":
            return 30

    # random shuffle to change moves chosen when same piece evaluation
    def random_shuffle(self,list):
        random.shuffle(list)
        return list