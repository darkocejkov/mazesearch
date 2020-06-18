import sys
import io
import array

class Node:
    coords = []         #tuple list containing grid coordinates
    pNode = None        #link to a Parent Node object
    manDist = 0         #calculated Manhattan Distance
    totalCost = 0       #totalCost = cost to path + manhattan distance

    def __init__(self, x, y, endPos=None, parentNode = None):
        self.coords = [x, y]
        self.pNode = parentNode
        self.manDist = abs(abs((x - endPos[0]))+abs((y - endPos[1])))

    def print_node(self):
        print(self.coords)