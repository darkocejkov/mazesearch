import sys
import io
import array
from maze import Maze
from queue import Queue
from node import Node

#performs algorithms (bfs, dfs, greedy best, a*)

def bfs(maze):
    #function that takes a maze as input and performs Breadth-first Search
    #BFS: explores all nodes of the same breadth (ie same depth/layer)
    maze.print_maze()
    #maze.print_directions()
    #we start at the starting position and check which directions we can traverse
    #then, we traverse 1 "node" in every possible directon
    iNode = maze.startPos #initial node (the start, P)
    iNode.print_node()
    q = Queue(10) #create a queue ... !!! what is a good max for this situation ?? !!!

    #TODO: implement nextNodes; start traversing the maze using nodes;
    #TODO: implement adjust, start queueing nodes
    
    

#def dfs(maze):
    #function that takes maze object as input and performs Depth-first Search

#def greedybest(maze)

#def astar(maze)