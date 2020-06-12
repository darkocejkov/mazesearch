#This file is meant to handle reading of the maze inputs

import sys
import io
import array

class Maze:
    height = 0
    width = 0
    mazeArray = [0]
    manDistance = 0
    startPos = [0,0]
    endPos = [0,0]

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
        #print(mazeLen)
        #print(maze)
        fp.close()

        height = int(mazeLen/width) #calculate height of maze by amount of chars divided by width
        self.height = height
        print(f"height: {height}, width: {width}, total chars: {mazeLen}")

        self.mazeArray = [[0 for x in range(width)] for y in range(height)]

        xind = 0
        yind = 0
        for char in maze:

            if(char == '\n'): #increment the row counter and reset col counter
                yind += 1
                xind = 0
                continue #skip this char
            else:
                #print(f"[{char},{xind},{yind}]", end='')
                #assign char to [row][col] within 2D array
                if(char == '%'):
                    self.mazeArray[yind][xind] = '■' #wall is now ■ (for clarity -- remove later)
                elif(char == ' '):
                    self.mazeArray[yind][xind] = '°'
                else:
                    if(char == 'P'):
                        self.startPos = [xind, yind]
                    elif(char == '.'):
                        self.endPos = [xind, yind]
                    self.mazeArray[yind][xind] = char
                xind+=1

        #self.manDistance = ???

    def print_maze(self): #prints the maze
        for x in range(self.height): #prints the mazeArray
            for y in range(self.width):
                print("%c " % str(self.mazeArray[x][y]), end='') #print 2D array looking niceeeeeee
            print()

    def positions(self): #func. that prints out the positions of the start and end (deprecated)
        print(f"start: {self.startPos[0]},{self.startPos[1]} end:{self.endPos[0]},{self.endPos[1]}")
        #print("[col, row]")
        print(f"{self.mazeArray[self.startPos[0]][self.startPos[1]]}")