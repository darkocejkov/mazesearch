#This file is meant to handle reading of the maze inputs

import sys
import io
import array

w = open("./resources/bigMaze.txt", "r")

wi = w.readline().replace('\n','')
#print(wi)
width = len(wi) #read first line from file to get the width of the maze
#print(width)
w.close() 

fp = open("./resources/bigMaze.txt", "r") 

maze = fp.read() #read entire maze from new file pointer
mazeStrip = maze.replace('\n','') #strip the maze of newline chars to get accurate reading of #chars
mazeLen = len(mazeStrip)
#print(mazeLen)
#print(maze)
fp.close()
    
height = int(mazeLen/width) #calculate height of maze by amount of chars divided by width
print(f"height: {height}, width: {width}, total chars: {mazeLen}")

#implement the maze into a 2D array?

mazeArray = [[0 for x in range(width)] for y in range(height)] #2D array to contain the maze
#print(mazeArray)

xind = 0
yind = 0
for char in maze:

    if(char == '\n'): #increment the row counter and reset col counter
        yind += 1
        xind = 0
        continue #skip this char
    else:
        #print(f"[{char},{xind},{yind}]", end='')
        mazeArray[yind][xind] = char #assign char to [row][col] within 2D array
        xind+=1


for x in range(height): #prints the mazeArray
    for y in range(width):
        print("%c " % str(mazeArray[x][y]), end='') #print 2D array looking niceeeeeee
    print()




# xind = 0
# yind = 0
# for char in maze:
    
#     if(char == '\n' or (xind == width - 1)):
#         print("yeet")
#         xind = 0
#         yind += 1
#     else:
#         mazeArray[xind][yind] = char
#         xind += 1

#     print(f"[{char}|{xind}|{yind}] ", end='')
#     mazeArray[xind][yind] = char
    
    
    

# for x in range(width):
#     for y in range(height):
        


