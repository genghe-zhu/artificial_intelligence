# Genghe Zhu
# CS 76, PA4
# Fall 2022

import math
from collections import defaultdict


class CircuitBoardLayout:
    def __init__(self, components, board_dimensions):

        #Each component is a list of point with (0,0) as lower left corner
        # bb ((0.0),(0,1),(1,0),(1,1),(2,0),(2,1)) c        aaa ((0,0), (0,1), (0,2)) 
        # bb                                      ccc  ((0,0),(0,1),(0,2),(0.3),(0,4),(1,1),
        # bb                                     ccccc (1,2),(1,3),(2,2))
        self.components = components

        # define dimensions
        # (0,0) is the bottom left corner (like coordinate axes)
        self.board_x = board_dimensions[0]
        self.board_y = board_dimensions[1]
        # variables will be locations of lower left corners for each component
        self.vars = []
        
        self.possible_domains = {}
        # saves the biggest x and biggest y dimension
        # ex: height and width for rectangle, or height and width for triangle
        self.component_size = {}
        # try rotate 90, 180, and 270 deg 
        # then checks if the flipped shape is the same as the original shape (if so it just removes)
        self.allow_rotations = {}

        # index for each component
        i = 0
        # since each component is so big, use an index as the key
        for component in self.components:
            self.component_size[i] = self.get_component_xy_size(self.components[i])
            self.generate_allow_rotations(i)
            self.possible_domains[i] = self.generate_possible_domains(i, self.component_size[i])
            #vars save component index
            self.vars.append(i)
            i += 1

        # every component has a constraint with each other
        # i.e. no component can overlap with each other
        self.constraints = defaultdict(dict)
        for c1 in range(i):   
            for c2 in range(i):
                if c1 != c2:
                    self.constraints[c1][c2] = 1
                    self.constraints[c2][c1] = 1

        # for __str__ function
        self.solution = None
        self.nodes_visited = 0
        self.var_heuristics_used = ""
        self.value_heuristics_used = ""
        self.ac3_used = "No"


    #Get max x, y of a component (component size)
    # used to check if we can allow rotations 
    def get_component_xy_size(self, component):
        x = (-1) * math.inf
        y = (-1) * math.inf
        for pair in component:
            if pair[0] > x:
                x = pair[0]
            if pair[1] > y:
                y = pair[1]

        # since we start at 0,0
        return (x+1, y+1)

    # generate allow rotation for each component, not repeating component after rotation
    def generate_allow_rotations(self, index):
        allow_rotation = [0]
        maxx = (self.component_size[index])[0] - 1
        maxy = (self.component_size[index])[1] - 1

        #rotate 180 degree
        points1 = []
        # rotate 90
        points2 = []
        # rotate 270
        points3 = []
        for point in self.components[index]:
            x = point[0]
            y = point[1]
            # rotations
            points1.append((y,x))
            points2.append((x, maxy - y))
            points3.append((y, maxx - x))

        # sort so that we can compare same shapes 
        self.components[index].sort()
        points1.sort()
        points2.sort()
        points3.sort()

        # don't add the same shapes that are flipped
        if points2 != self.components[index]:
            allow_rotation.append(2)

        if points1 != self.components[index]:
            allow_rotation.append(1)
            if points3 != points1:
                allow_rotation.append(3)

        self.allow_rotations[index] = allow_rotation.copy()


    #genereate possible domain/location for a component
    #(rotation, min_x, min_y)
    def generate_possible_domains(self, index, size):
        component_x = size[0]
        component_y = size[1]
        #domain is list of possible (rotation, minx, miny)
        domains = []

        for x in range (0, self.board_x - component_x + 1):
            for y in range (0, self.board_y - component_y + 1):
                d = (0, x, y)
                domains.append(d)
                #rotate 180 degree
                if 2 in self.allow_rotations[index]:
                    d = (2, x, y)
                    domains.append(d)

        #rotate the component x, y
        for x in range (0, self.board_x - component_y + 1):
            for y in range (0, self.board_y - component_x + 1):
                #rotate 90 degree
                if 1 in self.allow_rotations[index]:
                    d = (1, x, y)
                    domains.append(d)
                #rotate 270 degree
                if 3 in self.allow_rotations[index]:
                    d = (3, x, y)
                    domains.append(d)

        return domains

    #test if 2 component can be placed in domain1 and domain2
    #basically test if they overlap (test constraints)
    def allow(self, component_index1, component_index2, domain1, domain2):
        
        occupy_location1 = self.place_component(component_index1, domain1)
        occupy_location2 = self.place_component(component_index2, domain2)
        for x in occupy_location1:
            for y in occupy_location1[x]:
                if x in occupy_location2 and y in occupy_location2[x]:
                    return False #overlap
        return True #not overlap
    
    # places component on board
    def place_component(self, component_index, domain):
        component = self.components[component_index]
        occupy_location = defaultdict(dict)
        x = domain[1]
        y = domain[2]
        rotation = domain[0]
        maxx = (self.component_size[component_index])[0] - 1
        maxy = (self.component_size[component_index])[1] - 1

        for point in component:
            if rotation == 0:
                x1 = x + point[0]
                y1 = y + point[1]
            elif rotation == 1:#rotate x and y
                x1 = x + point[1]
                y1 = y + point[0]
            elif rotation == 2: #rotate 180 degree
                x1 = x + point[0]
                y1 = y + maxy - point[1]
            else:#rotate 270 degree
                x1 = x + point[1]
                y1 = y + maxx - point[0]
            occupy_location[x1][y1] = 1

        return occupy_location

    # to string method to print out result
    def __str__(self):
        result = "Circuit Board Layout Problem:\n"
        result += "Variable heuristic: "+ self.var_heuristics_used +"\n"
        result += "Domain heuristic: " + self.value_heuristics_used + "\n"
        result += "AC3 used: " + self.ac3_used + "\n"
        result += "Number of Calls: " + str(self.nodes_visited) + "\n"
        if self.solution == False:
            result += "No Solution Found\n"
        else:
            result += "Solution: \n"
            result += self.print_board()
        return result

    # helper function for to string
    def print_board(self):
        board = [['.' for x in range(self.board_x)] for y in range(self.board_y)]
        
        for index in self.solution:
            (rotation, x, y) = self.solution[index]
            component = self.components[index]
            maxx = (self.component_size[index])[0] - 1
            maxy = (self.component_size[index])[1] - 1
            if rotation == 0: #not rotated, capital letter
                char_num = 65 + index
            else: # rotated, lower letter
                char_num = 97 + index
       
            for point in component:
                if rotation == 0:
                    x1 = x + point[0]
                    y1 = y + point[1]
                elif rotation == 1:#rotate 90 degree, switch    x and y
                    x1 = x + point[1]
                    y1 = y + point[0]
                elif rotation == 2: #rotate 180 degree
                    x1 = x + point[0]
                    y1 = y + maxy - point[1]
                else:#rotate 270 degree
                    x1 = x + point[1]
                    y1 = y + maxx - point[0]
                
                board[y1][x1] = chr(char_num)

        board_str = ""
        for y in range(self.board_y - 1, -1, -1):
            for x in range (0, self.board_x):
                board_str += board[y][x]
            board_str += "\n"

        return board_str
                    





        