#hw5q3

from ArrayStack import *
from ArrayDeque import *

class MidStack():
    def __init__(self):
        self.data1 = ArrayStack()
        self.data2 = ArrayDeque() 
        
    def __len__(self):
        return len(self.data1) + len(self.data2)

    def is_empty(self):
        return len(self) == 0

    def push(self, item):
        self.data2.enqueue_last(item)
        if len(self.data2) > len(self.data1):
            self.data1.push(self.data2.dequeue_first())

    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        if self.data2.is_empty():
            return self.data1.top()
        else:
            return self.data2.last()

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        if self.data2.is_empty():
            return self.data1.pop()
        else:
            return self.data2.dequeue_last()

    def mid_push(self,item):
        if len(self.data1) - 1 == len(self.data2):
            self.data2.enqueue_first(item)
        elif len(self.data1) == len(self.data2):
            self.data1.push(item)

def main():
    midS = MidStack()
    midS.push(2)
    midS.push(4)
    midS.push(6)
    midS.push(8)
    midS.push(10)
    midS.mid_push(12)
    print(midS.pop())
    print(midS.pop())
    print(midS.pop())
    print(midS.pop())
    print(midS.pop())
    print(midS.pop())
