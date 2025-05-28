# Genghe Zhu
# CS 76, PA4
# Fall 2022

from multiprocessing.dummy.connection import families
import Heuristics

# implemented backtracking search from the pseudo code in the slides
def backtracking_search(csp):
    csp.solution = recursive_backtracking({}, csp)
    return csp

# second part of pseudo code from slides
def recursive_backtracking(assignment, csp):

    # nodes visited tracker (instance variable in MapColoring and CircuitBoardLayout)
    csp.nodes_visited += 1

    # base case (all variables assigned)
    if len(assignment) == len(csp.vars):
        return assignment

    # get variable to search (potentially with heuristic)
    var = select_unassigned_variable(assignment, csp)

    # loop through domains of that variable (potentially with heuristic)
    for value in order_domain_values(var, assignment, csp):
        if consistent(var, value, assignment, csp):
            # keep a copy of possible domains in case assigning value doesn't work out (reaches dead end, so need to backtrack)
            possible_domains_copy = csp.possible_domains.copy()
            assign_var_value(var, value, assignment, csp)

            # to run without AC3: comment out lines 34 and 41-44, and left indent lines 35-40
            if AC3(csp):
                if recursive_backtracking(assignment, csp):
                    return assignment
                else:
                    # remove the assignment and reset domain
                    del assignment[var]
                    csp.possible_domains = possible_domains_copy.copy()
            else:
                # remove the assignment and reset domain
                del assignment[var]
                csp.possible_domains = possible_domains_copy.copy()
    # no solution case
    return False

# called by recursive_backtracking
# check if assigning the value to that variable is consistent with the other assignments
def consistent(var, value, assignment, csp):
    for neighbor in csp.constraints[var]:
        # make sure neighbor isn't already assigned
        if neighbor in assignment.keys():
            # allow() checks if assigning value to var and neighbor_value to neighbor works
            # this is different for the two problems, so we must define it separately
            if not csp.allow(var, neighbor, value, assignment[neighbor]):
                return False
    return True

# helper function for recursive backtracking
def assign_var_value(var, value, assignment, csp):
    assignment[var] = value
    csp.possible_domains[var] = [value]
    # loop through neighbors and update domain
    for neighbor in csp.constraints[var]:
        neighbor_possible_domains = []
        for neighbor_value in csp.possible_domains[neighbor]:
            # allow() checks if assigning value to var and neighbor_value to neighbor works
            # this is different for the two problems, so we must define it separately
             if csp.allow(var, neighbor, value, neighbor_value):
                 neighbor_possible_domains.append(neighbor_value)

        csp.possible_domains[neighbor] = neighbor_possible_domains     

# arc consistency
# called in recursive backtracking
def AC3(csp):
    csp.ac3_used = "Yes"
    arcs = []
    # add all the constraints into arcs
    # ex: NSW boarders V, V also boarders NSW
    for var in csp.constraints:
        for neighbor in csp.constraints[var]:
            arcs.append((var, neighbor))

    while len(arcs) > 0:
        constraint = arcs.pop(0)
        # test possible_domains of constraint[0] against constraint
        # return true if possible_domains[constraint[0]] changed
        if (test_domain_constraint(constraint, csp)):
            if len(csp.possible_domains[constraint[0]]) == 0:
                return False
            for c1 in csp.constraints:
                # check if the variable is in the rhs of constraints
                if constraint[0] in csp.constraints[c1]:
                    pair = (c1, constraint[0])
                    # add "flipped" constraint to arcs if it doesn't already exist
                    if pair not in arcs:
                        arcs.append(pair)

    return True

# helper function for AC3
# test if the current domain changes after testing constraint
def test_domain_constraint(constraint, csp):
    var = constraint[0]
    neighbor = constraint[1]
    changed_possible_domains = False

    # loop through possible domain for a variable
    for value in csp.possible_domains[var]:
        value_remove = True
        for neighbor_value in csp.possible_domains[neighbor]:
            
            # if allow domain pair for variable pair
            # i.e. if both var can take on value AND neighbor can take on neighbor_value
            # without violating any constraints 
            if csp.allow(var, neighbor, value, neighbor_value):
            # if (value, neighbor_value) in csp.constraints[var][neighbor]:
                value_remove = False
                break

        if value_remove:
            csp.possible_domains[var].remove(value)
            changed_possible_domains = True

    return changed_possible_domains

# variable heuristics 
def select_unassigned_variable(assignment, csp):
    # uncomment the heuristic desired, get_next_var is the baseline (no heuristic)
    method = Heuristics.get_next_var
    # method = Heuristics.mrv_heuristic
    # method = Heuristics.degree_heuristic

    # this is for the print results function
    csp.var_heuristics_used = method.__name__
    return method(assignment, csp)

# value heuristics
def order_domain_values(var, assignment, csp):
    # uncomment the heuristic desired, get_next_var is the baseline (no heuristic)
    method = Heuristics.get_domain
    # method = Heuristics.lcv_heuristic

    # this is for the print results function
    csp.value_heuristics_used = method.__name__
    return method(var, assignment, csp)
