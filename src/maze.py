#This file is meant to handle reading of the maze inputs

import sys
import io
import array

class Maze:
    height = 0              #integer holding the value of the height of the maze (ie. how many rows in the array)
    width = 0               #integer holding the value of the width of the maze (ie. how many columns in the array)
    mazeArray = [0]         #array that holds the maze
    mazeDirections = [0]    #array that holds a vector for every square, indicating which directions are possible to traverse in
    manDistance = 0         #integer value that is the Manhattan distance (sum of x and y directions) from the start to the end position
    startPos = [0,0]        #array vector holding the coords of the start position
    endPos = [0,0]          #array vector holding the coords of the end position
    wallChar = '■'
    spaceChar = '°'

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
        print(f"height: {height}, width: {width}, total chars: {mazeLen}")

        self.mazeArray = [[0 for x in range(width)] for y in range(height)]
        self.mazeDirections = [[[0 for i in range(4)] for x in range(width)] for y in range(height)]

        xind = 0
        yind = 0
        for char in maze:

            if(char == '\n'): #increment the row counter and reset col counter
                yind += 1 
                xind = 0
                continue #skip this char, don't put it into the array since we change rows by incrementing y-index
            else:
                #print(f"[{char},{xind},{yind}]", end='')
                #assign char to [row][col] within 2D array
                if(char == '%'):
                    self.mazeArray[yind][xind] = self.wallChar #wall is now ■ (for clarity -- can remove later)
                elif(char == ' '):
                    self.mazeArray[yind][xind] = self.spaceChar #indicate the empty spaces, since we are printing with padding for clarity
                else:
                    if(char == 'P'):
                        self.startPos = [xind, yind]
                    elif(char == '.'):
                        self.endPos = [xind, yind]
                    self.mazeArray[yind][xind] = char
                xind+=1

        #we must do this seperately from populating the maze array since the data of neighbours isn't fully populated
            #unless we did it with a buffer or something, but that's a little too complex
        #now we must populate the direction data via the 3D array
        #traverse thru the 2D maze array
        #then, for every square we check neighbouring squares and input the data

        #traverse 2D maze
        for x in range(self.height): #rows
            for y in range(self.    width): #cols
                currentSquare = self.mazeArray[x][y]
                #if(currentSquare != self.wallChar):
                    #check up (make sure to not check out of list bounds by making sure x != 0 or x != height)
                        #[row-1][col]
                    #check down
                        #[row+1][col]
                    #check left
                        #[row][col-1]
                    #check right
                        #[row][col+1]
                    
                

        self.manDistance = abs((self.startPos[0] - self.endPos[0]) + (self.startPos[1] - self.endPos[1])) #calculate the manhattan distance [y1 - x1] + [y2 - y1]
        print(f"manhattan dist: {self.manDistance}")

    def print_maze(self): #prints the maze
        for x in range(self.height): #prints the mazeArray
            for y in range(self.width):
                print("%c " % str(self.mazeArray[x][y]), end='') #print 2D array
            print()

    def print_directions(self): #prints the mazeArray
        for x in range(self.height): #rows
            for y in range(self.width): #columns
                print("[",end='')
                for z in range(4):
                    print("%c," % str(self.mazeDirections[x][y][z]), end='') #print 3D array
                print("]",end='')
            print("|")
    

    def positions(self): #func. that prints out the positions of the start and end (deprecated)
        print(f"start: {self.startPos[0]},{self.startPos[1]} end:{self.endPos[0]},{self.endPos[1]}")
        #print("[col, row]")
        print(f"{self.mazeArray[self.startPos[0]][self.startPos[1]]}")