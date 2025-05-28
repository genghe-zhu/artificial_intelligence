# Genghe Zhu
# CS 76, PA4
# Fall 2022


from collections import defaultdict

class MapColoring:

    def __init__(self, vars, domain, constraints):
        self.vars = vars
        self.domain = domain
        # initiate constraints so that it can take 2 keys (i.e. 2d dictionary)
        self.constraints = defaultdict(dict)
        # constraint = 1 meanst that constraint exists
        for c in constraints:   
            self.constraints[c[0]][c[1]] = 1
            self.constraints[c[1]][c[0]] = 1

        # for __str__ function
        self.solution = None
        self.nodes_visited = 0
        self.var_heuristics_used = ""
        self.value_heuristics_used = ""
        self.ac3_used = "No"

        # for AC3
        self.possible_domains = {}
        for var in self.vars:
            self.possible_domains[var] = domain.copy()

    # helper function for AC3, tests var = value and neighbor = neighbor value
    # i.e. if both var can take on value AND neighbor can take on neighbor_value
    # without violating any constraints 
    def allow(self, var, neighbor, value, neighbor_value):
        if self.constraints[var][neighbor] == 1 and value == neighbor_value:
            return False
        return True

    # to string function
    def __str__(self):
        result = "Map Coloring Problem:\n"
        result += "Variable heuristic: "+ self.var_heuristics_used +"\n"
        result += "Domain heuristic: " + self.value_heuristics_used + "\n"
        result += "AC3 used: " + self.ac3_used + "\n"
        result += "Number of Calls: " + str(self.nodes_visited) + "\n"
        if self.solution == False:
            result += "No Solution Found\n"
        else:
            result += "Solution: " + str(self.solution) + "\n"
        return result