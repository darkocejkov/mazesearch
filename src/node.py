

class Node:
    coords = []

    def __init__(self, x, y):
        self.coords = [x, y]

    def node_x(self):
        return self.coords[0]
    
    def node_y(self):
        return self.coords[1]

    def print_node(self):
        print(self.coords)

    
