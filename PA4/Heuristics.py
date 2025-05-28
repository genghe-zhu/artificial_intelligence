# Genghe Zhu
# CS 76, PA4
# Fall 2022

import math

# Variable Heuristics

# simple no heuristics
def get_next_var(assignment, csp):
    for var in csp.vars:
        if var not in assignment:
            return var

# minimum remaining values heuristic
# choose the vairable with the fewest legal values
def mrv_heuristic(assignment, csp):
    var_fewest_legal_values = None
    # set variable to store the fewest legal values 
    min_legal_values = math.inf
    # loop through all the variables that aren't assigned yet
    for var in csp.vars:
        if var not in assignment:
            # get the number of legal values by looking at the domain
            num_legal_values = len(csp.possible_domains[var])

            # comparison 
            if num_legal_values < min_legal_values:
                var_fewest_legal_values = var
                min_legal_values = num_legal_values

    return var_fewest_legal_values

# the variable with the most number of neighbors
# helper function for degree_heuristic
def num_constraints(var, assignment, csp):
    counter = 0
    for neighbor in csp.constraints[var]:
        if neighbor not in assignment:
            counter += 1
    
    return counter

# choose variable with the most constraints on the remaining variables 
def degree_heuristic(assignment, csp):
    var_most_constraints = None
    most_num_constraints = -1 * math.inf
    # loop through the variables 
    for var in csp.vars:
        if var not in assignment:
            # call helper function to count number of constraints
            constraint_num = num_constraints(var, assignment, csp)
            if constraint_num > most_num_constraints:
                var_most_constraints = var
                most_num_constraints = constraint_num

    return var_most_constraints

# Domain Heuristics

# simple no heuristic
def get_domain(var, assignment, csp):
    return csp.possible_domains[var]

# least constraining value (LCV) heuristic
def lcv_heuristic(var, assignment, csp):
    domain_sums = {}
    #(R, G, B)-> value = R
    for value in csp.possible_domains[var]:
        sum = 0
        for neighbor in csp.constraints[var]:
            if neighbor not in assignment.keys():
                #(R,B), (R,G), (B, G)..
                for neighbor_value in csp.possible_domains[neighbor]:
                    # if allow domain pair for variable pair
                    # i.e. if both var can take on value AND neighbor can take on neighbor_value
                    # without violating any constraints 
                    if csp.allow(var, neighbor, value, neighbor_value):
                        sum += 1   

        domain_sums[value] = sum
    # returns keys of sorted dictionary, sorted from greatest to least
    sorted_domain = dict(sorted(domain_sums.items(), key=lambda item: item[1], reverse=True))
    return sorted_domain.keys()

