#Driver for the main program
"""
QUESTION:
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

The deliverables for each maze in combination with each algorithm:
    - display the path on the maze by putting a '.' in the path of the maze
    - path cost as sol. (# of steps taken to get from start to finish)
    - # of nodes expanded by each algorithm.
"""

import sys
import io
from maze import Maze
from algo import bfs,dfs,greedybest,a_star

#load both mazes into their respective objects
#2nd arg. is the debug for the "visit" function
    #should be the same as debug value for the alg.
bigMaze = Maze("./resources/bigMaze.txt", 0)
medMaze = Maze("./resources/mediumMaze.txt", 0)

#first param is the maze to run the algo. on
#second is the debugging prints (1 = on, 0 = off)

bfs(medMaze, 0)
bfs(bigMaze, 0)

#we reload the maze files in order to reset arrays and set values
#so that the previous algorithm doesn't affect the next
bigMaze = Maze("./resources/bigMaze.txt", 0)
medMaze = Maze("./resources/mediumMaze.txt", 0)
dfs(medMaze, 0)
dfs(bigMaze, 0)

bigMaze = Maze("./resources/bigMaze.txt", 0)
medMaze = Maze("./resources/mediumMaze.txt", 0)
greedybest(medMaze, 0)
greedybest(bigMaze, 0)

bigMaze = Maze("./resources/bigMaze.txt", 0)
medMaze = Maze("./resources/mediumMaze.txt", 0)
a_star(medMaze, 0)
a_star(bigMaze, 0)