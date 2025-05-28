# Genghe Zhu
# CS76, PA3
# Fall 2022

from AlphaBetaAI import AlphaBetaAI

class IterativeDeepening:

    # constructor
    def __init__(self, depth):
        self.depth = depth
    
    # choose move
    def choose_move(self, board):
        chosen_move = None
        
        print("Iterative deepening with AlphaBetaAI for depth = " + str(self.depth))

        # loop through the different depths 
        for i in range(1, self.depth + 1):
            ai = AlphaBetaAI(i)
            chosen_move = ai.choose_move(board)

        # print the best moves for each depth
        print("Best move for depth = " + str(self.depth) + ": " + str(chosen_move))

        return chosen_move