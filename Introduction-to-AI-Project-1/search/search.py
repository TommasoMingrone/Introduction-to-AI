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
import heapq
from collections import deque

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
    """
    start_state = problem.getStartState()
    visited = set()

    stack = util.Stack()
    stack.push((start_state, []))

    while not stack.isEmpty():
        current_state, actions = stack.pop()

        if current_state in visited:
            continue

        visited.add(current_state)

        if problem.isGoalState(current_state):
            return actions

        successors = problem.getSuccessors(current_state)
        for next_state, action, _ in successors:
            if next_state not in visited:
                stack.push((next_state, actions + [action]))

    return []



def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    """
    start_state = problem.getStartState()
    if problem.isGoalState(start_state):
        return []  # The start state is the goal state

    # Initialize a queue for BFS
    queue = util.Queue()

    visited = set()  # Initialize a set to keep track of visited states

    queue.push((start_state, []))  # Enqueue the initial state with an empty action list

    while not queue.isEmpty():
        state, actions = queue.pop()

        if state in visited:
            continue  # Skip already visited states

        visited.add(state)

        if problem.isGoalState(state):
            return actions  # We found the goal

        for next_state, action, _ in problem.getSuccessors(state):
            new_actions = actions + [action]
            queue.push((next_state, new_actions))

    return []  # If no solution is found, return an empty list




def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    visited = set()
    priority_queue = util.PriorityQueue()
    start_state = problem.getStartState()

    # Each element in the priority queue is a tuple: (state, path, cost)
    priority_queue.push((start_state, [], 0), 0)

    while not priority_queue.isEmpty():
        current_state, path, cost = priority_queue.pop()

        if problem.isGoalState(current_state):
            return path

        if current_state not in visited:
            visited.add(current_state)

            for successor, action, step_cost in problem.getSuccessors(current_state):
                new_path = path + [action]
                new_cost = cost + step_cost
                priority_queue.push((successor, new_path, new_cost), new_cost)

    return None  # Return None if no solution is found


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    visited = set()
    priority_queue = util.PriorityQueue()
    start_state = problem.getStartState()

    # Each element in the priority queue is a tuple: (state, path, cost)
    priority_queue.push((start_state, [], 0), 0)

    while not priority_queue.isEmpty():
        current_state, path, cost = priority_queue.pop()

        if problem.isGoalState(current_state):
            return path

        if current_state not in visited:
            visited.add(current_state)

            for successor, action, step_cost in problem.getSuccessors(current_state):
                new_path = path + [action]
                new_cost = cost + step_cost
                heuristic_cost = new_cost + heuristic(successor, problem)

                priority_queue.push((successor, new_path, new_cost), heuristic_cost)

    return None  # Return None if no solution is found







# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
