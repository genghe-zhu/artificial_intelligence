from MazeworldProblem import MazeworldProblem
from Maze import Maze

from uninformed_search import bfs_search
from astar_search import astar_search

# null heuristic, useful for testing astar search without heuristic (uniform cost search).
def null_heuristic(state):
    return 0

# Test problems

# test_maze3 = Maze("maze3.maz")
# test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))

# print(test_mp.get_successors(test_mp.start_state))

# # this should explore a lot of nodes; it's just uniform-cost search
# result = astar_search(test_mp, null_heuristic)
# print(result)

# result = astar_search(test_mp, test_mp.euclidean_heuristic)
# print(result)
# test_mp.animate_path(result.path)

# # this should do a bit better:
# result = astar_search(test_mp, test_mp.manhattan_heuristic)
# print(result)
# test_mp.animate_path(result.path)

# test A* works on 5x5 maze
# test_maze_rand = Maze("maze5x5_1rob.maz")
# test_5x5 = MazeworldProblem(test_maze_rand, (4,4))
# result = astar_search(test_5x5, null_heuristic)
# print(result)
# result = astar_search(test_5x5, test_5x5.euclidean_heuristic)
# print(result)
# result = astar_search(test_5x5, test_5x5.manhattan_heuristic)
# print(result)
# test_5x5.animate_path(result.path)

# test A* works on no solution 10x10 maze
# test_maze_rand = Maze("maze_10x10_no_sol.maz")
# maze_10x10_no_sol = MazeworldProblem(test_maze_rand, (9,9))
# result = astar_search(maze_10x10_no_sol, null_heuristic)
# print(result)
# result = astar_search(maze_10x10_no_sol, maze_10x10_no_sol.euclidean_heuristic)
# print(result)
# result = astar_search(maze_10x10_no_sol, maze_10x10_no_sol.manhattan_heuristic)
# print(result)
# maze_10x10_no_sol.animate_path(result.path)

# test A* works on no solution 40x40 maze
# test_maze_rand = Maze("maze_40x40.maz")
# maze_40x40 = MazeworldProblem(test_maze_rand, (2,39,2,38))
# # result = astar_search(maze_40x40, null_heuristic)
# # print(result)
# result = astar_search(maze_40x40, maze_40x40.euclidean_heuristic)
# print(result)
# result = astar_search(maze_40x40, maze_40x40.manhattan_heuristic)
# print(result)

# test A* works on no solution 20x20 maze
# test_maze_rand = Maze("maze_20x20.maz")
# maze_20x20 = MazeworldProblem(test_maze_rand, (15, 0, 7, 4, 13, 14))
# result = astar_search(maze_40x40, null_heuristic)
# print(result)
# result = astar_search(maze_20x20, maze_20x20.euclidean_heuristic)
# print(result)
# result = astar_search(maze_20x20, maze_20x20.manhattan_heuristic)
# print(result)

# Your additional tests here:
test_maze_rand = Maze("maze_test_work.maz")
test_rand = MazeworldProblem(test_maze_rand, (0, 10, 1, 0, 2, 0))
result = astar_search(test_rand, null_heuristic)
print(result)
result = astar_search(test_rand, test_rand.euclidean_heuristic)
print(result)
result = astar_search(test_rand, test_rand.manhattan_heuristic)
print(result)
test_rand.animate_path(result.path)

