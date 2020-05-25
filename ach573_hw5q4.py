#hw5q4

from ArrayStack import *

class Queue():
    def __init__(self):
        self.data1 = ArrayStack()
        self.data2 = ArrayStack()
        
    def __len__(self):
        return len(self.data1)

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self,item):
        self.data1.push(item)

    def dequeue(self):
        if (self.is_empty()):
            raise Exception("Queue is empty!") 
        while not (self.is_empty()):
            self.data2.push(self.data1.pop())
        elem = self.data2.pop()
        for i in range(len(self.data2)):
            self.data1.push(self.data2.pop())
        return elem 

    def first(self):
        if (self.is_empty()):
            raise Exception("Queue is empty!") 
        while not (self.is_empty()):
            self.data2.push(self.data1.pop())
        elem = self.data2.pop()
        self.data1.push(elem) 
        for i in range(len(self.data2)):
            self.data1.push(self.data2.pop())
        return elem 


class Queue1():
    def __init__(self):
        self.data = ArrayStack()

    def enqueue(self, item):
        last = item
        self.data.push([item, last])

    def dequeue(self):
        return self.data.pop()[1] 


def main():
    q = Queue1()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    print(q.dequeue())

main()
