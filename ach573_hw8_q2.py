#hw8q2

from BinarySearchTreeMap import *

def create_chain_bst(n):
    bst = BinarySearchTreeMap() 
    for i in range(1,n+1):
        bst.insert(i)
    return bst

def create_complete_bst(n):
    bst = BinarySearchTreeMap()
    add_items(bst, 1, n)
    return bst

def add_items(bst,low,high):
    if low > high:
        return bst
    else: 
        mid = ((high + low) // 2)
        bst.insert(mid)
        add_items(bst,low,mid-1)
        add_items(bst,mid+1,high)


def main():
    x = create_complete_bst(7)
    #print(x.root.left.right.item.key)
    print(x.root.item.key)
    for elem in x:
        print(elem)
    
#main()
