
from collections import deque
from email.mime import base
from platform import node
from SearchSolution import SearchSolution
from treelib import Node, Tree



# you might find a SearchNode class useful to wrap state objects,
#  keep track of current depth for the dfs, and point to parent nodes
class SearchNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, parent=None):
        # you write this part
        self.state = state
        self.parent = parent

    # backchaining helper method for when solution is found in BFS
    def backchaining(self, search_problem, search_method, num_nodes_visited):
        solution = SearchSolution(search_problem, search_method)
        path = []
        
        curr_node = self
        # loop up until start node (ie has no parents)
        while curr_node.parent != None:
            path.insert(0, curr_node.state)
            curr_node = curr_node.parent

        path.insert(0, search_problem.start_state) # add initial start state
        solution.path = path
        # add total number of nodes visited to solution 
        solution.nodes_visited = num_nodes_visited
        return solution


# added another parameter that is default set to false for printing out a tree with treelib
def bfs_search(search_problem, tree_visual = False):
    # initialize tree for visualizing BFS if tree_visual is true
    if tree_visual:
        tree = Tree()

    frontier = deque() # BFS is FIFO so we use a queue
    already_visited_states = set() # set for graph search (don't visit same state twice)

    # set start node and add it to visualization tree
    start_node = SearchNode(search_problem.start_state)
    if tree_visual:
        tree.create_node(start_node.state, start_node.state)

    frontier.append(start_node)
    already_visited_states.add(start_node.state)


    num_nodes_visited = 0 # for printing solution in SearchSolution

    # loop until frontier is empty
    while frontier:
        curr_node = frontier.popleft()
        curr_state = curr_node.state

        num_nodes_visited += 1 # count total number of nodes visited for SearchSolution

        # test if current state is the goal state, call backchaining method in SearchNode class, and display the tree
        if search_problem.goal_test(curr_state):
            if tree_visual:
                tree.show()
            return curr_node.backchaining(search_problem, "BFS", num_nodes_visited)

        # call get_successors method from FoxProblem
        for child in search_problem.get_successors(curr_state):
            child_node = SearchNode(child, curr_node)
            # since this is graph search, check if child node was already visited, if not add to frontier 
            if not child_node.state in already_visited_states:
                frontier.append(child_node)
                already_visited_states.add(child_node.state)
                # add node to tree visual 
                if tree_visual:
                    tree.create_node(child_node.state, child_node.state, parent=curr_state)

    # no solution case when all the nodes have been visited
    no_solution = SearchSolution(search_problem, "BFS")
    no_solution.nodes_visited = num_nodes_visited
    # display the tree
    if tree_visual:
        tree.show()
    return no_solution


# my DFS solution has two extra parameters: tree_visual and tree
# tree visual is set by the user if they want to see the tree that DFS searched in the output
# tree is to pass the visualized tree in each recursive call
def dfs_search(search_problem, tree_visual = False, depth_limit=100, node=None, solution=None, tree=None):
    # if no node object given, create a new search from starting state
    if node == None:
        node = SearchNode(search_problem.start_state)
        solution = SearchSolution(search_problem, "DFS")

        # initiate visual tree
        if tree_visual:
            tree = Tree()
            # add start node (no parent)
            tree.create_node(str(node.state), str(node.state))

    # Base case 1: reach depth limit
    if depth_limit == 0:
        return False
    # Base case 2: the node has been visited before
    if node.state in solution.path:
        return False

    # if the node has not been visited and depth not reached, add the node to a potential solution list
    solution.path.append(node.state)
    solution.nodes_visited += 1

    # Base case 3: reached goal state, so we visualize tree and return solution
    if search_problem.goal_test(node.state):
        if tree_visual:
            tree.create_node(str(node.state), str(node.state), parent = str(node.parent))
            tree.show()
        return solution
    
    # edge case for when dfs needs to insert the same node twice within the same sub-branch (treelib gets confused)
    if tree_visual:
        if node.parent != None:
            # check if the node is already in the tree
            # if so, the node will have a number behind it
            # ex: (2,2,0) already exists, so when we need to add (2,2,0) to a branch again, it will be added as (2,2,0),35
            # the 35 is just an arbitrary unique number (the # nodes visited), so that we can add multiple (2,2,0)s
            if tree.get_node(str(node.state)):
                node_name = str(node.state) + ", " + str(solution.nodes_visited)
            else:
                node_name = str(node.state)
            
            tree.create_node(node_name, node_name, parent = str(node.parent))

    # check the child nodes and recursively call dfs_search at depth - 1
    for child in search_problem.get_successors(node.state):
        child_node = SearchNode(child, node.state)

        result = dfs_search(search_problem, tree_visual, depth_limit - 1, child_node, solution, tree)
        if result:
            return result

    # if the solution is not in the branch, remove the nodes recursively
    solution.path.remove(node.state)

    # visualize the tree in the failure state
    if node.state == search_problem.start_state:
        if tree_visual:
            tree.show()
        return solution


# ids search just calls dfs_search()
def ids_search(search_problem, tree_visual = False, depth_limit=100):
    solution = SearchSolution(search_problem, "IDS")
    # loop through the depth limits from 1 to depth_limit + 1 (instead of 0 to depth_limit)
    for i in range(1, depth_limit + 1):
        
        # each depth, visualize the tree
        if tree_visual:
            print("depth: " + str(i))

        # run DFS search and add to the total number of nodes visited
        result = dfs_search(search_problem, tree_visual, i)
        solution.nodes_visited += result.nodes_visited

        if tree_visual:
            print("# nodes visited: " + str(result.nodes_visited) + "\n")

        # success case if the solution exists at this depth
        if len(result.path) > 0:
            solution.path = result.path
            return solution

    # failure case 
    return solution

    
    
