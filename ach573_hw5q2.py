#hw5q2

from ArrayStack import *

class MaxStack():
    def __init__(self):
        self.data = ArrayStack()

    def __len__(self):
        return len(self.data) 

    def is_empty(self):
        return len(self) == 0

    def push(self, item):
        if self.is_empty() or self.data.top()[1] <= item:
            val = tuple([item, item])
        elif self.data.top()[1] > item:
            val = tuple([item, self.data.top()[1]])
        self.data.push(val)

    def top(self):
        if (self.is_empty() == True):
            raise Exception("Stack is empty!")
        return self.data.top()[0]

    def pop(self):
        if (self.is_empty() == True):
            raise Exception("Stack is empty!")
        return self.data.pop()[0]

    def max(self):
        if (self.is_empty() == True):
            raise Exception("Stack is empty!")
        return self.data.top()[1]

def main():
    maxS = MaxStack()
    maxS.push(3)
    maxS.push(1)
    maxS.push(6)
    maxS.push(4)
    print(maxS.max())
    print(maxS.pop())
    print(maxS.pop())
    print(maxS.max())
    print(maxS.top())
