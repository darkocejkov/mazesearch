#This file is meant to handle reading of the maze inputs

import sys
import io

fp = open("./resources/mediumMaze.txt", "r")

maze = fp.read()

maze[25] = "X"

print(maze)