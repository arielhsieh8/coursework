#hw5q5

from ArrayStack import *
from ArrayQueue import *

def permutations(lst):
    res_lst = []
    q = ArrayQueue()
    for elem in lst:
        q.enqueue([elem])
    while not(q.is_empty()):
        finish = True
        s = ArrayStack()
        val = q.dequeue()
        for i in range(len(lst)):
            if lst[i] not in val:
                s.push(lst[i])
                finish = False
        while not(s.is_empty()):
            new_lst = val + [s.pop()]
            q.enqueue(new_lst)
        if finish:
            res_lst.append(val)
    return res_lst

def main():
    lst = [1]
    x = permutations(lst)
    print(x)

main()
            
        
        
        
        
