#Driver for the main program
"""
A Pacman agent is meant to find a path through the maze and avoid ghosts.
The maze is given via text file, where '%' is a wall, 'P' is the start, and '.' is the goal.
Step costs are equal to one.

Use 
    [uninformed]
    Depth-first search, 
    breadth-first search, 
    
    [informed]
    greedy best-first search, 
    A* search.
        - use Manhattan distance

The deliverables for each maze (medium & large) in combination with each algorithm:
    - display the path on the maze by putting a '.' in the path of the maze
    - path cost as sol. (# of steps taken to get from start to finish)
    - # of nodes expanded by each algorithm.

"""

import sys
import io
from maze import Maze

#load both mazes into their respective objects
bigMaze = Maze("./resources/bigMaze.txt")
bigMaze.print_maze()
bigMaze.positions()

medMaze = Maze("./resources/mediumMaze.txt")
medMaze.print_maze()
medMaze.positions()
#medMaze.print_directions()

"""
ideas:
- 2D array to hold the maze itself
- another 2D of the same size that holds directional info about each square of the maze
    -   which directions we can move in AND how many actions?
    -   ex. [up, down, left, right]
        - for which each direction will be a boolean indicating that it is possible to traverse that way

- calculating distance between P and . for manhattan distance (for informed algos)
    - by their positions within the maze
    - we know that the first and last rows are purely walls
    - we also know that the first and last columns are walls
    - must also calculate manhattan distance for every square

- tree or graph?
- can either generate a tree by traversing and organizing the directions we can go by states
- or we can traverse the maze directly as a graph
    - BFS traversal
        - start at P, go in each direction possible (expanding P node)
        - from every node visited, move all possible directions
    - DFS traversal
        - from P pick a direction that is traversable, continue expanding the deepest node

"""