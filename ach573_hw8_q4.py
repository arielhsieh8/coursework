#hw8q4

from BinarySearchTreeMap import *

def find_min_abs_difference(bst):
    lst = []
    for elem in bst.inorder():
        lst.append(elem.item.key)
    min_val = abs(lst[1] - lst[0])
    for i in range(1,len(lst)-1):
        if abs(lst[i+1] - lst[i]) < min_val:
            min_val = abs(lst[i+1] - lst[i])
    return min_val

def main():
    bst = BinarySearchTreeMap()
    bst.insert(15)
    bst.insert(10)
    bst.insert(4)
    bst.insert(1)
    bst.insert(6)
    bst.insert(20)
    bst.insert(17)
    bst.insert(25)
    x = find_min_abs_difference(bst)
    print(x)

#main()
