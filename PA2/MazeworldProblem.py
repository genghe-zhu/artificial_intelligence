from Maze import Maze
from time import sleep

class MazeworldProblem:

    ## you write the constructor, and whatever methods your astar function needs

    def __init__(self, maze, goal_locations):
        self.maze = maze
        self.goal_locations = goal_locations
        # start with moving robot 0
        self.start_state = tuple([0])
        # loop through maze to find the initial positions of all the robots
        for i in range(0, maze.width):
            for j in range(0, maze.width):
                if maze.has_robot(i, j):
                    self.start_state = (*self.start_state, i)
                    self.start_state = (*self.start_state, j)


    def __str__(self):
        string =  "Mazeworld problem: "
        return string

    def get_successors(self, locations):
        # make sure robot locations are the same as our inputted locations
        # or else, our check_move function would not work properly
        self.maze.robotloc = locations[1:]
        
        successors = []

        # the first element of locations tells which robot to move
        robot_num = locations[0]

        # make a list of copy of locations, which is a tuple
        # since we cannot change tuples (immutable), save as list
        list_locations = list(locations)

        # add state of staying put, and moving onto next robot
        # if robot the last robot, move first robot
        if list_locations[0] + 1 == (len(list_locations) - 1)/2:
            list_locations[0] = 0
        else :
            list_locations[0] += 1
        successors.append(tuple(list_locations))

        # possible moves for robot in N,S,E,W directions
        possible_moves = [(1,0), (-1,0), (0,1), (0,-1)]
        curr_x = robot_num * 2 + 1
        curr_y = robot_num * 2 + 2

        # loop through the possible moves 
        for move in possible_moves:
            if self.check_move(list_locations[curr_x] + move[0], list_locations[curr_y] + move[1]):
                # move robot to new direction, append it to possible successors
                list_locations[curr_x] += move[0]
                list_locations[curr_y] += move[1]
                successors.append(tuple(list_locations))
                # move back to original location and try other directions
                list_locations[curr_x] -= move[0]
                list_locations[curr_y] -= move[1]
        
        return successors

    # check if robot can move to location x,y legally
    def check_move(self, x, y):
        # check if robot moves out of the maze
        if x < 0 or x > self.maze.width or y < 0 or y > self.maze.height:
            return False
        # check to see if robot moves into a wall
        if not self.maze.is_floor(x, y):
            return False
        # check to see if robot moves to same location as other robot
        if self.maze.has_robot(x, y):
            return False
        return True
        

    # check if robot has reached its goal
    def goal_test(self, locations):
        return self.goal_locations == locations[1:len(locations)]

    # uniform move cost function for a* search
    def move_cost(self, state, new_state):
        # check if the robot moved --> cost = 1
        if state[1:len(state)] != new_state[1:len(new_state)]:
            return 1
        return 0

    # manhattan heuristic function for A*
    def manhattan_heuristic(self, state):
        curr_locations = state[1:]
        heuristic_cost = 0

        # add the absolute value of the differences
        for i in range(len(self.goal_locations)):
            distance = abs(curr_locations[i] - self.goal_locations[i])
            heuristic_cost += distance

        return heuristic_cost

    # euclidian heuristic function for A*
    def euclidean_heuristic(self, state):
        curr_locations = state[1:]
        heuristic_cost = 0

        # add using the function (x^2 + y^2)^(1/2)
        for i in range(0, len(self.goal_locations) - 1, 2):
            # x squared distance
            distance = (curr_locations[i] - self.goal_locations[i]) ** 2
            # add y squared distance
            distance += (curr_locations[i + 1] - self.goal_locations[i + 1]) ** 2
            # square root of sum of squared x and y distance
            distance = distance ** 0.5
            # add to total heuristic cost
            heuristic_cost += distance
            
        return heuristic_cost

    # given a sequence of states (including robot turn), modify the maze and print it out.
    #  (Be careful, this does modify the maze!)

    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state[1:])

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state[1:])
            sleep(1)

            print(str(self.maze))


## A bit of test code. You might want to add to it to verify that things
#  work as expected.

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

    # test from starting position
    # print(test_maze3)
    # print(test_mp.get_successors((0, 1, 0, 1, 1, 2, 1)))
    # print(test_mp.get_successors((1, 1, 0, 1, 1, 2, 1)))
    # print(test_mp.get_successors((2, 1, 0, 1, 1, 2, 1)))


    print(test_mp.get_successors((1, 1, 0, 1, 2, 2, 1)))




    
