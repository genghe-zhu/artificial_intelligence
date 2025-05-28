class FoxProblem:
    def __init__(self, start_state=(3, 3, 1)):
        self.start_state = start_state
        self.goal_state = (0, 0, 0)
        self.total_chicken = start_state[0]
        self.total_fox = start_state[1]

        # you might want to add other things to the problem,
        #  like the total number of chickens (which you can figure out
        #  based on start_state

    
    # get successor states for the given state
    def get_successors(self, state):
        # you write this part. I also had a helper function
        #  that tested if states were safe before adding to successor list
        successor_list = []
        # possible moves: 2 chickens on boat, 1 chicken, 2 foxes, 1 fox, 1 fox + 1 chicken
        possible_move_list = [(-2, 0), (-1, 0), (0, -2), (0, -1), (-1, -1)]
        
        # test the possible moves and add to successor_list if safe
        for move in possible_move_list:
            new_state = self.try_move(state, move)
            if self.safe_state(new_state):
                successor_list.append(new_state)

        return successor_list


    def try_move(self, state, move):
        if (state[2] == 1):
            return (state[0] + move[0], state[1] + move[1], 0)
        else:
            return (state[0] - move[0], state[1] - move[1], 1)

    def safe_state(self, state):
        # check enough chicken and fox to move left to right and right to left
        if (state[0] >= 0 and state[1] >= 0 and self.total_chicken - state[0] >= 0
            and self.total_fox - state[1] >= 0):
            # check if the left side is safe (more chicken than foxes)
            if (state[0] == 0 or state[0] >= state[1]):
                # check if the right side is safe (more chicken than foxes)
                if (self.total_chicken - state[0] == 0 or 
                    self.total_chicken - state[0] >= self.total_fox - state[1]):
                    return True
        return False

    # I also had a goal test method. You should write one.
    def goal_test(self, state):
        if (state[0] == 0 and state[1] == 0 and state[2] == 0):
            return True
        return False

    def __str__(self):
        string =  "Chickens and foxes problem: " + str(self.start_state)
        return string


## A bit of test code

if __name__ == "__main__":
    test_basic = FoxProblem((3,3,1))
    print(test_basic.get_successors((3, 3, 1)))
    print(test_basic)

    test_cp = FoxProblem((5, 5, 1))
    print(test_cp.get_successors((5, 5, 1)))
    print(test_cp)
