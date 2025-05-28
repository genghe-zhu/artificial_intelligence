from mmap import ACCESS_DEFAULT
import random

# generates a random maze given dimensions, number of robots, and percent of tiles to be obstacles
def gen_maze(width, height, num_robot, pct_obstacle):
    robot_locations = []
    # initiate a maze full of obstacles (no floor tiles)
    maze = [['#' for y in range(height)] for x in range(width)]

    # first randomly place the robots
    for i in range(num_robot):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        while maze[x][y] == ".":
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
        maze[x][y] = '.'
        robot_locations.append(x)
        robot_locations.append(y)

    # then change obstacle tiles to floor tiles based on pct_obstacle argument
    for i in range(width):
        for j in range(height):
            if maze[i][j] != '.':
                # using a random distribution, it changes "#" tiles into "." tiles
                if random.randint(0,100) > pct_obstacle:
                    maze[i][j] = '.'

    # it then checks that each robot is not totally boxed in and has moves to make (at least intially)
    for i in range(0, len(robot_locations) - 1, 2):
        robot_x = robot_locations[i]
        robot_y = robot_locations[i + 1]
        maze = check_local_solvable(robot_x, robot_y, maze)
        
    return (maze, robot_locations)
    
# function to print maze
def print_maze(maze, robot_locations):
    maze_width = len(maze)
    maze_height = len(maze[0])
    # tricky part is that my random mazes are stored as 2d arrays, while the mazes are traversed by x and y
    for j in range(maze_height):
        line = ""
        for i in range(maze_width):
            line = line + str(maze[i][maze_height - j - 1])
        print(line)
    print(robot_locations)

# function that checks if robots are not totally boxed in
def check_local_solvable(x, y, maze):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    counter = 0
    
    # counts the initial number of obstacles or walls around robots
    for move in moves:
        neighbor_x = x + move[0]
        neighbor_y = y + move[1]
        if (neighbor_y < 0 or neighbor_y > len(maze[0]) - 1 
           or neighbor_x < 0 or neighbor_x > len(maze) - 1):
            counter += 1
        elif maze[neighbor_x][neighbor_y] == '#':
            counter += 1

    # if there are 4 walls/obstacles around a robot, then randomly replace one of them with a "."
    while counter == 4:
        rand_num = random.randint(0,3)
        neighbor_x = x + moves[rand_num][0]
        neighbor_y = y + moves[rand_num][1]
        # checks if maze is now locally solvable
        if not (neighbor_y < 0 or neighbor_y > len(maze[0]) - 1 
           or neighbor_x < 0 or neighbor_x > len(maze) - 1):
            counter -= 1
            maze[neighbor_x][neighbor_y] = '.'
    return maze
        
# prints our 2d array generated maze into a .maz file so that we can run our other files on it
def file_output(maze, robot_locations, filename):
    file = open(filename, "w")
    width = len(maze)
    height = len(maze[0])

    # first prints the raw maze (no robots)
    for j in range(height):
        line = ""
        for i in range(width):
            line = line + str(maze[i][height - j - 1])
        file.write(line + "\n")

    # then prints the robot locations
    for i in range(0, len(robot_locations) - 1, 2): 
        file.write("\\robot " + str(robot_locations[i]) + " " + str(robot_locations[i+1]) + "\n")

    file.close()

# some testing code 
if __name__ == "__main__":
    width = 20
    height = 20
    num_robots = 3
    pct_obstacle = 30
    (maze, robot_locations) = gen_maze(width, height, num_robots, pct_obstacle)
    
    print_maze(maze, robot_locations)

    file = file_output(maze, robot_locations, "maze_test.maz")


