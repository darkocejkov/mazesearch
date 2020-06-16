import sys
import io
import array

class Node:
    coords = []
    pNode = None
    #cNode = None

    def __init__(self, x, y, parentNode = None):
        self.coords = [x, y]
        self.pNode = parentNode

    def node_x(self):
        return self.coords[0]
    
    def node_y(self):
        return self.coords[1]

    def print_node(self):
        print(self.coords)

    # def parent(self, n):
    #     #function that parents a node to another
    #     self.parentNode = n



    
