import sys
import array
import io

class Queue:
    maxi = 0
    size = 0
    front = 0
    back = 0
    queue = [0]

    def __init__(self, m):
        self.queue = [None for x in range(m)]
        self.maxi = m
        self.size = 0
        self.front = 0
        self.back = 0
        
    #n is a "node", which is simply just an object that carries coordinates
    def push(self, n):
        if(self.is_full()):
            print("error [push]: queue is full")
        else:
            self.queue[self.back] = n
            self.size +=1
            self.back += 1

    def pop(self):
        if(self.is_empty()):
            print("error [pop]: queue is empty")
        else:
            n = self.queue[self.front]
            self.queue[self.front] = 0
            self.size -= 1
            self.front += 1
            return n  
        

    #def adjust(self):
        #use to adjust the queue indices, whenever the front nears the end of the queue index
        #use inside push()

    def is_empty(self):
        return self.size == 0

    def is_full(self):
        return self.size == self.maxi

    def print_queue(self):
        print("[",end='')
        for x in range(self.maxi):
            print(f"{self.queue[x]},", end='')
        print("]")