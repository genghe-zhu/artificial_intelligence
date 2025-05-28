from FoxProblem import FoxProblem
from uninformed_search import bfs_search, dfs_search, ids_search

# Create a few test problems:
problem111 = FoxProblem((1, 1, 1))
problem221 = FoxProblem((2, 2, 1))
problem331 = FoxProblem((3, 3, 1))
problem541 = FoxProblem((5, 4, 1))
problem551 = FoxProblem((5, 5, 1))
problem_big = FoxProblem((20, 15, 1))

# Run the searches.
#  Each of the search algorithms should return a SearchSolution object,
#  even if the goal was not found. If goal not found, len() of the path
#  in the solution object should be 0.

tree_visual = False # set this to False if you don't want the tree graph
# print(bfs_search(problem111, tree_visual))
# print(dfs_search(problem111, tree_visual))
# print(ids_search(problem111, tree_visual))

# print(bfs_search(problem221, tree_visual))
# print(dfs_search(problem221, tree_visual))
# print(ids_search(problem221, tree_visual))

# print(bfs_search(problem331, tree_visual))
# print(dfs_search(problem331, tree_visual))
print(ids_search(problem331, tree_visual))

# print(bfs_search(problem551, tree_visual))
# print(dfs_search(problem551, tree_visual))
print(ids_search(problem551, tree_visual))

# print(bfs_search(problem541, tree_visual))
# print(dfs_search(problem541, tree_visual))
print(ids_search(problem541, tree_visual))

# print(bfs_search(problem_big, tree_visual))
# print(dfs_search(problem_big, tree_visual))
# print(ids_search(problem_big, tree_visual))