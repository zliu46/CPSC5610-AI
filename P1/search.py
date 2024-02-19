# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    fringe = util.Stack()
    visited_node = set()  # Store state that is visited
    start_node = (problem.getStartState(), [], 0)  # Initialize a start node
    fringe.push(start_node)
    while not fringe.isEmpty(): # check if fringe is empty
        node, path, cost = fringe.pop()
        if problem.isGoalState(node):
            return path
        if node not in visited_node:
            visited_node.add(node) # add node to visted list
            successors = problem.getSuccessors(node)
            for next_node, next_action, next_cost in successors:
                total_cost = cost + next_cost
                total_path = path + [next_action]
                total_state = (next_node, total_path, total_cost)
                fringe.push(total_state)
            
    util.raiseNotDefined()
   
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    queue = util.Queue()
    visited_node = set()  # Store state that is visited
    start_node = (problem.getStartState(), [], 0)  # Initialize a start node
    queue.push(start_node)
    while not queue.isEmpty():
        (node, path, cost) = queue.pop()
        if problem.isGoalState(node):
            return path
        if not node in visited_node:
            visited_node.add(node)
            for next_node, next_action, next_cost in problem.getSuccessors(node):
                totalCost = cost + next_cost
                totalPath = path + [next_action]
                totalState = (next_node, totalPath, totalCost)
                queue.push(totalState)
    util.raiseNotDefined()
    
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    priorityQueue = util.PriorityQueue()
    visited_node = set()  
    start_node = (problem.getStartState(), [], 0)  
    priorityQueue.push(start_node,0)
    while not priorityQueue.isEmpty():
        (node, path, cost) = priorityQueue.pop()
        if problem.isGoalState(node):
            return path
        if not node in visited_node:
            visited_node.add(node)
            for next_node, next_action, next_cost in problem.getSuccessors(node):
                totalCost = cost + next_cost
                totalPath = path + [next_action]
                totalState = (next_node, totalPath, totalCost)
                priorityQueue.push(totalState,totalCost)

    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    priorityQueue = util.PriorityQueue()
    visited_node = set()  
    start_node = (problem.getStartState(), [], 0)  
    priorityQueue.push(start_node, heuristic(problem.getStartState(), problem))
    while not priorityQueue.isEmpty():
        node, actions, cost = priorityQueue.pop()
        if problem.isGoalState(node):
            return actions
        if node not in visited_node:
            visited_node.add(node)
            for next_node, next_action, next_cost in problem.getSuccessors(node):
                totalCost = cost + next_cost
                totalPath = actions + [next_action]
                totalState = (next_node, totalPath, totalCost)
                priorityQueue.push(totalState, totalCost + heuristic(next_node, problem))
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
