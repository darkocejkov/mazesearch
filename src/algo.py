import sys
import io
import array
import time
from maze import Maze
from queue import Queue
from node import Node

#performs algorithms (bfs, dfs, greedy best, a*)

def bfs(maze):

    #initialize frontier queue (nodes to visit), and step cost (starting at 1 to account for the goal node)
    step_cost = 1
    frontier = []
    maze.print_maze()
    nodes_expanded = 0

    #start at the initial state, append it to the queue and mark it as visited
    start = maze.startPos
    frontier.append(start)
    maze.visit(start)
    
    #loop until there are no more nodes to visit
    while(frontier):
        s = frontier.pop(0) #pop the frontmost node
        nextNodeArray = maze.nextNodes(s) #assess that nodes visitable neighbours

        parent = maze.mazeNodes[s[0]][s[1]] #call this node the parent
        
        for i in nextNodeArray: #loop through the node's neighbours
            nodes_expanded += 1
            if(i == maze.endPos): #if the goal is found based on position, break out of the loop
                child = maze.mazeNodes[i[0]][i[1]]
                child.pNode = parent
                break

            if(maze.visit(i)): #'visit' those nodes by marking them and inserting into the queue
                frontier.append(i)

                #for every unvisited node, make the link of whichever node they're from to become their parent
                child = maze.mazeNodes[i[0]][i[1]]
                child.pNode = parent #the parent of this node is the one that we came from
        
        
        #time.sleep(0.01)        #illustrate updates to the BFS
        #maze.print_maze()
    
    child = maze.mazeNodes[maze.endPos[0]][maze.endPos[1]]
    while(child.pNode != None): #the last child node is the goal (because of the break)
        maze.mazeArray[child.coords[0]][child.coords[1]] = '.' #illustrate the solution
        #child.print_node()
        child = child.pNode #traverse the parent link

        #time.sleep(0.1)        #illustrate updates of the maze SOLUTION
        #maze.print_maze()

        step_cost += 1
    #maze.mazeArray[child.coords[0]][child.coords[1]] = '.'

    maze.print_maze()  #print the finished maze + solution and searched squares
    print(f"step cost of solution: {step_cost}")
    print(f"nodes expanded: {nodes_expanded}")

#def dfs(maze):
    #function that takes maze object as input and performs Depth-first Search

#def greedybest(maze)

#def astar(maze)