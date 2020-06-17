#This file is meant to handle reading of the maze inputs

import sys
import io
import array
from node import Node
from queue import Queue

class Maze:
    height = 0              #integer holding the value of the height of the maze (ie. how many rows in the array)
    width = 0               #integer holding the value of the width of the maze (ie. how many columns in the array)
    mazeArray = [0]         #array that holds the maze
    mazeDirections = [0]    #array that holds a vector for every square, indicating which directions are possible to traverse in
    mazeVisited = [0]       #bool array that holds 0/1 for every square, indicating if it has been visited
    mazeNodes = []          #Node array that holds the position of a Node object
    manDistance = 0         #integer value that is the Manhattan distance (sum of x and y directions) from the start to the end position
    startPos = [0,0]        #node holding the coords of the start position
    endPos = [0,0]          #node holding the coords of the end position
    wallChar = '%'#'■'
    spaceChar = ' '#'○'#' '
    goalChar = '.'
    upInd = 0
    downInd = 1
    leftInd = 2
    rightInd = 3
    acceptableNode = [spaceChar, goalChar] #array that holds characters we can traverse

    def __init__(self, filename): #constructor that reads maze file, and puts it into an array
        w = open(filename, "r")
        wi = w.readline().replace('\n','')
        width = len(wi) #read first line from file to get the width of the maze
        w.close()
        self.width = width

        fp = open(filename, "r") 

        maze = fp.read() #read entire maze from new file pointer
        mazeStrip = maze.replace('\n','') #strip the maze of newline chars to get accurate reading of #chars
        mazeLen = len(mazeStrip)
        fp.close()

        height = int(mazeLen/width) #calculate height of maze by amount of chars divided by width
        self.height = height

        #array comprehension to correctly size the arrays
        self.mazeArray = [[0 for x in range(width)] for y in range(height)]
        self.mazeDirections = [[[0 for i in range(4)] for x in range(width)] for y in range(height)]
        self.mazeVisited = [[0 for x in range(width)] for y in range(height)]
        self.mazeNodes = [[0 for x in range(width)] for y in range(height)]

        #i have it inverted, x should be y and y should be x
        #im not sure why it still works lol
        xind = 0
        yind = 0
        for char in maze:
            if(char == '\n'): #increment the row counter and reset col counter
                yind += 1 
                xind = 0
                continue #skip this char
            else:
                if(char == '%'):
                    self.mazeArray[yind][xind] = self.wallChar #wall is now ■ (for clarity -- can remove later)
                    #self.mazeArray[xind][yind] = self.wallChar
                elif(char == ' '):
                    self.mazeArray[yind][xind] = self.spaceChar #indicate the empty spaces, since we are printing with padding for clarity
                    #self.mazeArray[xind][yind] = self.spaceChar
                elif(char == '.'):
                    self.mazeArray[yind][xind] = self.goalChar
                    self.endPos = [yind, xind]
                else:
                    if(char == 'P'):
                        self.startPos = [yind, xind]
                    self.mazeArray[yind][xind] = char
                xind+=1

        #populate 2D node array to have correct nodes with correct parents
        #if we didn't keep this array, we'd have no way to correctly know any Node's parent
        for x in range(0, self.height):
            for y in range(0, self.width):
                self.mazeNodes[x][y] = Node(x, y, endPos=self.endPos, parentNode=None)

        
        #populate the 3D directions array to indicate possible neighbouring nodes we can visit
        #[up, down, left, right]
        for x in range(1, self.height-1): #rows 
            for y in range(1, self.width-1): #cols (check from 1 to width-1 because we know those are walls)
                #and so that we don't have to do error correction for out of list indices
                currentSquare = self.mazeArray[x][y]
                if(currentSquare != self.wallChar):
                    #check up (make sure to not check out of list bounds by making sure x != 0 or x != height)
                        #[row-1][col]
                    if(self.mazeArray[x-1][y] in self.acceptableNode):
                        self.mazeDirections[x][y][self.upInd] = 1
                    #check down
                    if(self.mazeArray[x+1][y] in self.acceptableNode):
                        #[row+1][col]
                        self.mazeDirections[x][y][self.downInd] = 1
                    #check left
                        #[row][col-1]
                    if(self.mazeArray[x][y-1] in self.acceptableNode):
                        self.mazeDirections[x][y][self.leftInd] = 1
                    #check right
                        #[row][col+1]
                    if(self.mazeArray[x][y+1] in self.acceptableNode):
                        self.mazeDirections[x][y][self.rightInd] = 1

    #print the maze
    def print_maze(self): 
        for x in range(self.width): 
            for y in range(self.height):
                print("%c " % str(self.mazeArray[x][y]), end='') 
            print()
        

    #print the 2D visited array (nodes that have been visisted)
    def print_visited(self): 
        for x in range(self.height): 
            for y in range(self.width):
                print("%c " % str(self.mazeVisited[x][y]), end='') 
            print()

    #print the 2D node array that contains Node objects
    def print_mazeNodes(self): 
        for x in range(self.width): 
            for y in range(self.height):
                currN = self.mazeNodes[x][y]
                currN.print_node() #doesn't print cleanly, is for debugging
            print()

    #print the 3D maze directions array
    def print_directions(self): 
        for x in range(self.width): 
            for y in range(self.height): 
                print("[",end='')
                for z in range(4):
                    print("%c," % str(self.mazeDirections[x][y][z]), end='') #print 3D array
                print("]",end='')
            print("|")

    #action to "visit" a node n, first checking if it already has been visited
    def visit(self, n):
        #n is a node
        if(self.mazeVisited[n[0]][n[1]] == 1):
            return 0
        else:
            self.mazeVisited[n[0]][n[1]] = 1
            if(self.mazeArray[n[0]][n[1]] != 'P'):
                #self.mazeArray[n[0]][n[1]] = '●' #to illustrate the search algo
                self.mazeArray[n[0]][n[1]] = '○'
            return 1

    #calculate distance between 2 nodes (arrays) (Manhattan Distance)
    def calcDistance(self, x, y):
        dist = abs((x[0] - y[0]) + (x[1] - y[1])) #manhattan distance = [y1 - x1] + [y2 - y1]
        return dist

    #compares 2 nodes, they are equal if both indices are the same
    def compare(self, n1, n2):
        return (n1[0] == n2[0] and n1[1] == n2[1])
    
    #determines the neighbouring nodes of n, and returns them as coordinates in an array
    def nextNodes(self, n):
        q = []
        curr = self.mazeDirections[n[0]][n[1]]
        if(curr[0] == 1): #up
            q.append([n[0]-1, n[1]])
        # if(curr[2] == 1): #left
        #     q.append([n[0], n[1]-1])
        if(curr[1] == 1): #down
            q.append([n[0]+1, n[1]])
        if(curr[2] == 1): #left
            q.append([n[0], n[1]-1])
        if(curr[3] == 1): #right
            q.append([n[0], n[1]+1])
        return q