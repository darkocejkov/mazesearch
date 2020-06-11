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
from mazearray import read_maze

read_maze("./resources/bigMaze.txt")