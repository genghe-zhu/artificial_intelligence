from mmap import ACCESS_DEFAULT
import random

def gen_maze(width, height, num_robot, pct_obstacle):
    robot_locations = []
    maze = [['#' for y in range(height)] for x in range(width)]

    for i in range(num_robot):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        while maze[x][y] == ".":
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
        maze[x][y] = '.'
        robot_locations.append(x)
        robot_locations.append(y)

    for i in range(width):
        for j in range(height):
            if maze[i][j] != '.':
                if random.randint(0,100) > pct_obstacle:
                    maze[i][j] = '.'

    for i in range(0, len(robot_locations) - 1, 2):
        robot_x = robot_locations[i]
        robot_y = robot_locations[i + 1]
        maze = check_local_solvable(robot_x, robot_y, maze)
        
    return (maze, robot_locations)
    
def print_maze(maze, robot_locations):
    maze_width = len(maze)
    maze_height = len(maze[0])
    for j in range(maze_height):
        line = ""
        for i in range(maze_width):
            line = line + str(maze[i][maze_height - j - 1])
        print(line + "\n")
    print(robot_locations)

def check_local_solvable(x, y, maze):
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    counter = 0
    
    for move in moves:
        neighbor_x = x + move[0]
        neighbor_y = y + move[1]
        if (neighbor_y < 0 or neighbor_y > len(maze[0]) - 1 
           or neighbor_x < 0 or neighbor_x > len(maze) - 1):
            counter += 1
        elif maze[neighbor_x][neighbor_y] == '#':
            counter += 1

    while counter == 4:
        rand_num = random.randint(0,3)
        neighbor_x = x + moves[rand_num][0]
        neighbor_y = y + moves[rand_num][1]
        if not (neighbor_y < 0 or neighbor_y > len(maze[0]) - 1 
           or neighbor_x < 0 or neighbor_x > len(maze) - 1):
            counter -= 1
            maze[neighbor_x][neighbor_y] = '.'
    return maze
        
def file_output(maze, robot_locations, filename):
    file = open(filename, "w")
    width = len(maze)
    height = len(maze[0])

    for j in range(height):
        line = ""
        for i in range(width):
            line = line + str(maze[i][height - j - 1])
        file.write(line + "\n")

    for i in range(0, len(robot_locations) - 1, 2): 
        file.write("\\robot " + str(robot_locations[i]) + " " + str(robot_locations[i+1]) + "\n")

    file.close()


if __name__ == "__main__":
    width = 
    height = 5
    num_robots = 1
    pct_obstacle = 70
    (maze, robot_locations) = gen_maze(width, height, num_robots, pct_obstacle)
    
    print_maze(maze, robot_locations)

    file = file_output(maze, robot_locations, "maze_test.maz")


