# You write this:
from SensorlessProblem import SensorlessProblem
from Maze import Maze
from astar_search import astar_search

print("Maze 1")
test_maze = Maze("maze1.maz")
test_problem = SensorlessProblem(test_maze)
result = astar_search(test_problem, test_problem.null_heuristic)
print(result)
result = astar_search(test_problem, test_problem.furthest_apart_heuristic)
print(result)
# test_problem.animate_path(result.path)

print("Maze 2")
test_maze = Maze("maze2.maz")
test_problem = SensorlessProblem(test_maze)
result = astar_search(test_problem, test_problem.furthest_apart_heuristic)
print(result)
# test_problem.animate_path(result.path)

print("Maze 3")
test_maze = Maze("maze3.maz")
test_problem = SensorlessProblem(test_maze)
result = astar_search(test_problem, test_problem.null_heuristic)
print(result)
result = astar_search(test_problem, test_problem.furthest_apart_heuristic)
print(result)
# test_problem.animate_path(result.path)

print("Maze 5x5 no solution")
test_maze = Maze("maze_5x5_no_sol.maz")
test_problem = SensorlessProblem(test_maze)
result = astar_search(test_problem, test_problem.null_heuristic)
print(result)
result = astar_search(test_problem, test_problem.furthest_apart_heuristic)
print(result)
# test_problem.animate_path(result.path)

# print("Maze 10x10 no solution")
# test_maze = Maze("maze_10x10_no_sol.maz")
# test_problem = SensorlessProblem(test_maze)
# result = astar_search(test_problem, test_problem.furthest_apart_heuristic)
# print(result)
# # test_problem.animate_path(result.path)

print("Maze 20x20")
test_maze = Maze("maze_20x20.maz")
test_problem = SensorlessProblem(test_maze)
result = astar_search(test_problem, test_problem.furthest_apart_heuristic)
print(result)
# test_problem.animate_path(result.path)

# print("Maze 40x40")
# test_maze = Maze("maze_40x40.maz")
# test_problem = SensorlessProblem(test_maze)
# result = astar_search(test_problem, test_problem.furthest_apart_heuristic)
# print(result)
# # test_problem.animate_path(result.path)