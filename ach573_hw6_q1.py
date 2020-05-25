#hw6q1

from DoublyLinkedList import *

class LinkedQueue():
    def __init__(self):
        self.data = DoublyLinkedList()

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self,item):
        self.data.add_last(item)

    def dequeue(self):
        if len(self) == 0:
            raise Exception("Queue is empty!") 
        return self.data.delete_first() 
        
    def first(self):
        if len(self) == 0:
            raise Exception("Queue is empty!") 
        return self.data.header.next.data


def main():
    q = LinkedQueue()
    q.enqueue(1)
    q.enqueue(2)
    print(q.dequeue())
    q.enqueue(3)
    print(q.dequeue())
    print(q.dequeue())
    print(q.first())

 
    
