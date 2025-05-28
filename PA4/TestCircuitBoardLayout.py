# Genghe Zhu
# CS 76, PA4
# Fall 2022

from CircuitBoardLayout import CircuitBoardLayout
from CSP import backtracking_search

# first three are simple test cases to make sure code works
test = CircuitBoardLayout([[(0, 0)], [(0, 0), (0, 1)], [(0, 0), (1, 0)], [(0, 0), (1, 0), (1, 1), (0, 1)]],
                          (3, 3))
result = backtracking_search(test)
print(result)

test = CircuitBoardLayout([[(0, 0)], [(0, 0), (0, 1)], [(0, 0), (0, 1)], [(0, 0), (1, 0), (1, 1), (0, 1)]],
                          (3, 3))
result = backtracking_search(test)
print(result)

test = CircuitBoardLayout([[(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2,2)], [(0, 0), (0, 1), (0, 2), (1, 1), (1, 2), (2,2)]],
                          (3, 4))
result = backtracking_search(test)
print(result)

# gradescope given example
test = CircuitBoardLayout([[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2)], [(0,0),(0,1),(0,2),(0,3),(0,4),(1,0),(1,1),(1,2),(1,3),(1,4)], 
                            [(0,0),(0,1),(1,0),(1,1),(2,0),(2,1)], [(0,0),(0,1),(0,2),(0,3),(0,4),(0,5),(0,6)]],
                          (10, 3))
result = backtracking_search(test)
print(result)

# harder test cases
test = CircuitBoardLayout([[(0, 0), (0, 1)], [(0, 0), (0, 1)], [(0, 0), (1, 0), (1, 1), (0, 1)],
                           [(0, 0), (0, 1), (0, 2), (1, 2)]],
                          (3, 4))
result = backtracking_search(test)
print(result)

# tetris
# pieces:
# a     b   cccc    dd  ee
# a     bb         dd    e
# aa    b               ee
# solution
# ACCCCEE
# AbbbDDE
# AAbDDEE
test = CircuitBoardLayout([[(0, 0), (0, 1), (0, 2), (1, 0)], [(0, 0), (1, 0), (2, 0), (1, 1)],
                           [(0, 0), (1, 0), (2, 0), (3, 0)], [(0, 0), (1, 0), (1, 1), (2, 1)],
                           [(0, 0), (1, 0), (1, 1), (0, 2), (1, 2)]],
                          (7, 3))
result = backtracking_search(test)
print(result)

# pieces:
# a     b    c   d  e     f
# aa    bb  cc  dd  eee fff
# solution:
# Efff
# EEEf
# ccdd
# AcBd
# AABB
test = CircuitBoardLayout([[(0,0),(1,0),(0,1)], [(0,0),(1,0),(0,1)], [(0,0),(1,0),(1,1)], [(0,0),(1,0),(1,1)],
                            [(0,0),(1,0),(2,0),(0,1)], [(0,0),(1,0),(2,0),(2,1)]],
                            (4,5))
result = backtracking_search(test)
print(result)