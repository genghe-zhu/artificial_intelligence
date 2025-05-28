from SearchSolution import SearchSolution
from heapq import heappush, heappop

class AstarNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, heuristic, parent=None, transition_cost=0):
        # you write this part
        self.state = state
        self.heuristic = heuristic
        self.parent = parent
        self.transition_cost = transition_cost

    def priority(self):
        # you write this part
        return self.heuristic + self.transition_cost

    # comparison operator,
    # needed for heappush and heappop to work with AstarNodes:
    def __lt__(self, other):
        return self.priority() < other.priority()


# take the current node, and follow its parents back
#  as far as possible. Grab the states from the nodes,
#  and reverse the resulting list of states.
def backchain(node):
    result = []
    current = node
    while current:
        result.append(current.state)
        current = current.parent

    result.reverse()
    return result


def astar_search(search_problem, heuristic_fn):
    # I'll get you started:
    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state))
    pqueue = []
    heappush(pqueue, start_node)

    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)

    visited_cost = {}
    visited_cost[start_node.state] = 0

    # you write the rest:

    # counter for number of nodes visited while conducting A* search
    num_visited = 0

    # keep looping until the queue is empty
    while pqueue:
        num_visited += 1
        # look at the node with the least cost in the sorted queue
        curr_node = heappop(pqueue)

        # check if the solution is a goal state
        if search_problem.goal_test(curr_node.state):
            solution.path = backchain(curr_node)
            solution.cost = curr_node.transition_cost
            solution.nodes_visited = num_visited
            return solution

        # loop through each child of current state
        for state in search_problem.get_successors(curr_node.state):

            # get cost of moving to each child (either 0 = not moving, or 1 = move)
            move_cost = search_problem.move_cost(curr_node.state, state)

            # if child is not explored, add child to explored
            # pack child into a node, with backpointer to current node
            # add node to frontier
            if not state in visited_cost:
                node = AstarNode(state, heuristic_fn(state), curr_node, curr_node.transition_cost + move_cost)
                heappush(pqueue, node)
                visited_cost[state] = curr_node.transition_cost
            else: 
                # else if child is in frontier with higher f
                # replace that frontier node with child node
                if curr_node.transition_cost < visited_cost[state]:
                    visited_cost[state] = curr_node.transition_cost
                    node = AstarNode(state, heuristic_fn(state), curr_node, curr_node.transition_cost + move_cost)
                    heappush(pqueue, node)

    # return no solution 
    solution.nodes_visited = num_visited
    return solution