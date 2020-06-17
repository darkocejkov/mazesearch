import sys
import io
import array

class Node:
    coords = []
    pNode = None
    manDist = 0

    def __init__(self, x, y, endPos=None, parentNode = None):
        self.coords = [x, y]
        self.pNode = parentNode
        self.manDist = abs((x - endPos[0]))+abs((y - endPos[1]))

    def node_x(self):
        return self.coords[0]
    
    def node_y(self):
        return self.coords[1]

    def print_node(self):
        print(self.coords)
    
    def get_dist(self):
        return self.manDist


    
