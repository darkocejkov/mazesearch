import sys
import io
import array
import time
from maze import Maze
from node import Node

#contains source codes for search algorithms

def bfs(maze, debug):

    print("------------- Breadth-first Search -------------")
    #initialize frontier queue (nodes to visit), and step cost (starting at 1 to account for the goal node)
    step_cost = 0
    frontier = []
    nodes_expanded = 0

    #start at the initial state, append it to the queue and mark it as visited
    start = maze.startPos
    frontier.append(start)
    maze.visit(start)
    found = 0
    
    #loop until there are no more nodes to visit
    while(frontier and not(found)):
        s = frontier.pop(0) #pop the frontmost node
        nextNodeArray = maze.nextNodes(s) #assess that nodes visitable neighbours
        if(debug):
            maze.mazeArray[s[0]][s[1]] = '●'
        parent = maze.mazeNodes[s[0]][s[1]] #call this node the parent
        nodes_expanded += 1
        for i in nextNodeArray: #loop through the node's neighbours
            
            if(i == maze.endPos): #if the goal is found based on position, break out of the loop
                child = maze.mazeNodes[i[0]][i[1]]
                child.pNode = parent
                found = 1
                break

            if(maze.visit(i)): #'visit' those nodes by marking them and inserting into the queue
                frontier.append(i)

                #for every unvisited node, make the link of whichever node they're from to become their parent
                child = maze.mazeNodes[i[0]][i[1]]
                child.pNode = parent #the parent of this node is the one that we came from
        
        if(debug):
            time.sleep(0.1)        #illustrate updates to the BFS
            maze.print_maze()
    
    child = maze.mazeNodes[maze.endPos[0]][maze.endPos[1]]
    while(child.pNode != None): #the last child node is the goal (because of the break)
        maze.mazeArray[child.coords[0]][child.coords[1]] = '.' #illustrate the solution
        #child.print_node()
        child = child.pNode #traverse the parent link

        if(debug):
            time.sleep(0.1)        #illustrate updates of the maze SOLUTION
            maze.print_maze()

        step_cost += 1
    #maze.mazeArray[child.coords[0]][child.coords[1]] = '.'

    maze.print_maze()  #print the finished maze + solution and searched squares
    print(f"BFS: step cost of solution: {step_cost}")
    print(f"BFS: nodes expanded: {nodes_expanded}")

def dfs(maze, debug):
    print("------------- Depth-first Search -------------")
    frontier = []
    step_cost = 0
    nodes_expanded = 0

    start = maze.startPos
    frontier.append(start)
    maze.visit(start)
    found = 0

    while(frontier and not(found)):
        s = frontier[-1] #-1 is the index of the last element in any array
        frontier.pop()
        if(debug):
            maze.mazeArray[s[0]][s[1]] = '●'
        nextNodeArray = maze.nextNodes(s)
        nodes_expanded += 1
        parent = maze.mazeNodes[s[0]][s[1]]

        #experimental:
        #nextNodeArray.reverse()

        for i in nextNodeArray:
            if(i == maze.endPos):
                found = 1
                child = maze.mazeNodes[i[0]][i[1]]
                child.pNode = parent
                break

            if(maze.visit(i)):
                child = maze.mazeNodes[i[0]][i[1]]
                child.pNode = parent
                frontier.append(i)

        if(debug):
            time.sleep(0.1)
            maze.print_maze()
    
    #maze.print_maze()

    child = maze.mazeNodes[maze.endPos[0]][maze.endPos[1]]
    while(child.pNode != None): #the last child node is the goal (because of the break)
        maze.mazeArray[child.coords[0]][child.coords[1]] = '.' #illustrate the solution
        child = child.pNode #traverse the parent link

        if(debug):
            time.sleep(0.1)        #illustrate updates of the maze SOLUTION
            maze.print_maze()

        step_cost += 1
    maze.print_maze()
    print(f"DFS: step cost of solution: {step_cost}")
    print(f"DFS: nodes expanded: {nodes_expanded}")

def greedybest(maze, debug):
    #use a Manhattan Distance calculation (heuristic function) to choose the best node (least distance)
    #priority queue based
    #   ie. cycle-sorted queue based on key
    print("------------- Best-first Search (Greedy) -------------")
    frontier = []
    step_cost = 0
    nodes_expanded = 0
    
    #start position represented by a Node object
    #in order to sort by manhattan distance
    start = maze.mazeNodes[maze.startPos[0]][maze.startPos[1]]
    frontier.append(start)
    maze.visit(start.coords)

    found = 0

    #in order to effectively have a 'priority queue', we need to sort the frontier
    #queue that contains Node objects now, instead of lists of coords.
    #and we insert Node objects into the list, and sort based on man. distance
    while(frontier and not(found)):
        frontier.sort(key=lambda x: x.manDist)
        # for x in frontier:
        #     print(f"{x.coords}:{x.manDist}")
        s = frontier.pop(0) #pop the frontmost node
        if(debug):
            maze.mazeArray[s.coords[0]][s.coords[1]] = '●'
        nextNodeArray = maze.nextNodes(s.coords) #expanding
        parent = maze.mazeNodes[s.coords[0]][s.coords[1]]
        nodes_expanded += 1

        for i in nextNodeArray:
            currN = maze.mazeNodes[i[0]][i[1]]
       
            #sorter.append(currN)
            if(i == maze.endPos):
                currN.pNode = parent
                found = 1
                break

            if(maze.visit(i)):
                currN.pNode = parent
                frontier.append(currN)
        if(debug):
            time.sleep(0.1)
            maze.print_maze()

    child = maze.mazeNodes[maze.endPos[0]][maze.endPos[1]]
    while(child.pNode != None): #the last child node is the goal (because of the break)
        maze.mazeArray[child.coords[0]][child.coords[1]] = '.' #illustrate the solution
        child = child.pNode #traverse the parent link

        if(debug):
            time.sleep(0.1)        #illustrate updates of the maze SOLUTION
            maze.print_maze()

        step_cost += 1
    maze.print_maze()
    print(f"BestFS: step cost: {step_cost}")
    print(f"BestFS: nodes expanded: {nodes_expanded}")

def a_star(maze, debug):
    #g(n) + h(n)
    #g(n) is the cost to reach the node
    #h(n) is the heuristic function (Manhattan Distance)

    #g(n) could possibly be a Node method, that traverses parent links
    #for every node within the next nodes (the neighbors)
    #and gives back the cost to reach that node
    #so we can add it to the manhattan distance
    #to achieve our heuristic, and then sort the list
    print("------------- A* -------------")
    frontier = []
    step_cost = 0
    nodes_expanded = 0
    found = 0

    start = maze.mazeNodes[maze.startPos[0]][maze.startPos[1]]
    frontier.append(start)
    maze.visit(start.coords)

    while(frontier and not(found)):
        frontier.sort(key=lambda x: x.totalCost)
        if(debug):
            for x in frontier:
                print(f"q={x.coords}:{x.totalCost}")
        s = frontier.pop(0) #pop the frontmost node
        if(debug):
            print(f"s={s.coords}:{s.totalCost}")
            maze.mazeArray[s.coords[0]][s.coords[1]] = '●'
        nextNodeArray = maze.nextNodes(s.coords) #expanding
        parent = maze.mazeNodes[s.coords[0]][s.coords[1]]
        nodes_expanded += 1

        for i in nextNodeArray:
            currN = maze.mazeNodes[i[0]][i[1]]
            
            if(i == maze.endPos):
                currN.pNode = parent
                found = 1
                break

            if(maze.visit(i)):
                cost = maze.path_cost(currN.coords) + 1
                currN.totalCost = currN.manDist + cost
                currN.pNode = parent
                frontier.append(currN)

            if(debug):
                time.sleep(0.1)
                maze.print_maze()
        

    child = maze.mazeNodes[maze.endPos[0]][maze.endPos[1]]
    while(child.pNode != None): #the last child node is the goal (because of the break)
        maze.mazeArray[child.coords[0]][child.coords[1]] = '.' #illustrate the solution
        #child.print_node()
        child = child.pNode #traverse the parent link

        if(debug):
            time.sleep(0.1)        #illustrate updates of the maze SOLUTION
            maze.print_maze()

        step_cost += 1
    maze.print_maze()

    print(f"A*: step cost: {step_cost}")
    print(f"A*: nodes expanded: {nodes_expanded}")