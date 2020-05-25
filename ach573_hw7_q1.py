#hw7q1

from LinkedBinaryTree import *

class EmptyTree(Exception):
    pass 

def min_and_max(bin_tree):
    if bin_tree.is_empty():
        raise EmptyTree()
    
    def subtree_min_and_max(root):
        if root.left is None and root.right is None:
            return (root.data, root.data)
        else:
            if root.left is None:
                left_tuple = (root.data, root.data)
            else: # if root.left is not None
                left_tuple = subtree_min_and_max(root.left)
            if root.right is None:
                right_tuple = (root.data, root.data) 
            else:
                right_tuple = subtree_min_and_max(root.right)
                
            min_val = min(left_tuple[0],right_tuple[0],root.data)
            max_val = max(left_tuple[1],right_tuple[1],root.data)
            
            return (min_val, max_val)
                
    return subtree_min_and_max(bin_tree.root)


def main():
    #l = LinkedBinaryTree()
    five = LinkedBinaryTree.Node(5)
    one = LinkedBinaryTree.Node(1)
    b = LinkedBinaryTree.Node(9,five,one)
    eight = LinkedBinaryTree.Node(8)
    four = LinkedBinaryTree.Node(4)
    c = LinkedBinaryTree.Node(7,eight,four)
    d = LinkedBinaryTree.Node(2,b,None)
    a = LinkedBinaryTree.Node(3,d,c)
    l = LinkedBinaryTree(a)
    w = LinkedBinaryTree()
##    for elem in l:
##        print(elem)
    x = min_and_max(w)
    print(x) 

#main() 
    
