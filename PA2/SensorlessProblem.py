from Maze import Maze
from time import sleep

class SensorlessProblem:

    ## You write the good stuff here:

    # constructor for sensorless problem
    def __init__(self, maze):
        self.maze = maze

        # look for all the possible starting locations (not walls or obstacles)
        starting_locations = []
        for i in range(maze.width):
            for j in range(maze.height):
                if maze.is_floor(i, j):
                    # add as coordinate to starting locations list
                    starting_locations.append((i, j))
        # initiate start state instance variable
        self.start_state = tuple(starting_locations)

    # get successors by trying moves up, down, left, right
    def get_successors(self, state):
        successors = []
        # possible moves are up, down, left, and right
        possible_moves = [(1,0), (-1,0), (0,1), (0,-1)]
        
        # try moves and add states for each direction
        for move in possible_moves:
            self.try_direction(move, state, successors)

        return successors

    # helper function for get successors
    def try_direction(self, move, state, successors):
        new_successors = []

        # loop through all the possible locations in a state
        for locations in state:
            loc_x = locations[0]
            loc_y = locations[1]
            move_x = move[0]
            move_y = move[1]

            # check if new move is a floor tile, if so add it (if it has not already been added)
            if self.maze.is_floor(loc_x + move_x, loc_y + move_y):
                if (loc_x + move_x, loc_y + move_y) not in new_successors:
                    new_successors.append((loc_x + move_x, loc_y + move_y))
                
            # if it is a wall/obstacle, add the original location (if it has not already been added)
            else:
                if (loc_x, loc_y) not in new_successors:
                    new_successors.append((loc_x, loc_y))
        # convert new successors to tuple
        successors.append(tuple(new_successors))

    def goal_test(self, state):
        # state with only one robot means reached goal
        return len(state) == 1

    # A* calls null heuristic with two parameters, so we add the second parameter here even though it is not used
    def null_heuristic(self, state):
        return 0

    # returns the total number of locations in state, but not an admissible heuristic
    def state_length_heuristic(self, state):
        return len(state)

    # three parameters because that is what A* calls for the Mazeworld problem
    def move_cost(self, state, new_state):
        return 1

    # another heuristic function
    def furthest_apart_heuristic(self, state):
        # set placeholder variables for the max and min x and y values
        max_x = 0
        max_y = 0
        min_x = self.maze.width
        min_y = self.maze.height

        # loop through each location and override if it is greater or less than our placeholders
        for s in state:
            if s[0] > max_x:
                max_x = s[0]
            if s[1] > max_y:
                max_y = s[1]
            if s[0] < min_x:
                min_x = s[0]
            if s[1] < min_y:
                min_y = s[1]

        # calculate the distance between the max and min for both y and x
        furthest_apart = (max_x - min_x) + (max_y - min_y)
        return furthest_apart

    def __str__(self):
        string =  "Blind robot problem: "
        return string


        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)

    # convert path from being a list of tuples of tuples into a list of tuples
    # this is so that the animate works
    def convert_path(self, path):
        converted_path = []
        for states in path:
            placeholder = []
            for tup in states:
                for t in tup:
                    placeholder.append(t)
            converted_path.append(tuple(placeholder))

        # input path should look like [((a,b), (c,d)), ((a,b))]
        # output converted path should look like [(a,b,c,d), (a,b)]

        return converted_path

    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state)

        path = self.convert_path(path)

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state)
            sleep(1)

            print(str(self.maze))

## A bit of test code

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_problem = SensorlessProblem(test_maze3)
