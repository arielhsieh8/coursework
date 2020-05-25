#hw8q3

from BinarySearchTreeMap import *

##def restore_bst(prefix_lst):
##    bst = BinarySearchTreeMap()
##    def restore_bst_helper(prefix_lst,low,high,root):
##        if low == high:
##            return BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(prefix_lst[low]))
##        else:
##            root = bst.root 
##            if prefix_lst[low+1] < prefix_lst[low]:
##                root.left = restore_bst_helper(prefix_lst, low+1, high, root.left)
##            elif prefix_lst[low+1] > prefix_lst[low]:
##                root.right = restore_bst_helper(prefix_lst, low+1, high, root.right)
##            return bst.Node()
####            bst.insert(prefix_lst[low])
####            restore_bst_helper(prefix_lst,low+1,high,bst)
####            return bst
##    return restore_bst_helper(prefix_lst, 0, len(prefix_lst)-1, bst)

##def restore_bst(prefix_lst):
##    bst = BinarySearchTreeMap()
##    def restore_bst_helper(prefix_lst):
##        root = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(prefix_lst[0]))
##        lst = [root]
##        for i in range(1,len(prefix_lst)): prefix_lst[1:]:
##            if prefix_lst[i] < lst[-1].item.key:
##                lst[-1].left = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(i))
##                lst.append(lst[-1].left)
##            else:
##                while(len(lst)>0 and lst[-1].item.key<i):
##                    last = lst.pop()
##                last.right = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(i))
##                lst.append(last.right)
##        return root
##    bst.root = restore_bst_helper(prefix_lst)
##    return bst


def restore_bst(prefix_lst):
    bst = BinarySearchTreeMap()
    def restore_bst_helper(prefix_lst, index, min_val, max_val):
        if index == len(prefix_lst):
            return root
        print(index)
        root = BinarySearchTreeMap.Node(BinarySearchTreeMap.Item(prefix_lst[index]))
        if prefix_lst[index] > min_val and prefix_lst[index] < max_val:
            print(prefix_lst[index], min_val, max_val, "hi")
            if prefix_lst[index+1] < prefix_lst[index]:
                max_val = prefix_lst[index] - 1
            else:
                min_val = prefix_lst[index-1] + 1
                max_val = prefix_lst[index+1]
            print(min_val, max_val)
            if index + 1 < len(prefix_lst):
                root.left = restore_bst_helper(prefix_lst, index+1, min_val, max_val )
        #elif prefix_lst[index] >= min_val and prefix_lst[index] >= max_val:
        print(prefix_lst[index], min_val, max_val)
            #min_val = root.parent.key + 1
        min_val = prefix_lst[0]
        max_val = prefix_lst[-1]
        if index+1 < len(prefix_lst):
            root.right = restore_bst_helper(prefix_lst, index+1, min_val, max_val)
        return root
    return restore_bst_helper(prefix_lst, 0, 0, prefix_lst[-1])


##def restore_bst(prefix_lst):
##    def restore_bst_helper(prefix_lst, key, low, high, size, index):
##        root = None
##        if index >= size:
##            return None
##        else:
##            print(key,low,high,index)
##            if key > low and key < high: 
##                root = BinarySearchTreeMap.Node(key)
##                index += 1 
##                if index < size:
##                    root.left = restore_bst_helper(prefix_lst, prefix_lst[index], low, key, size, index)
##                    #index += 1
##                    print(index)
##                    print(key,low,high)
##                    root.right = restore_bst_helper(prefix_lst, prefix_lst[index+1], key, high, size, index)
##                    print(index)
##            return root 
##    return restore_bst_helper(prefix_lst, prefix_lst[0], 0, prefix_lst[-1], len(prefix_lst), 0)


##def restore_bst_helper(pre, key, low, high, size, ind): 
##      
##    # Base Case 
##    if(ind >= size): 
##        return None
##  
##    root = None
##      
##    # If current element of pre[] is in range, then  
##    # only it is part of current subtree 
##    if(key > low and key < high): 
##  
##        # Allocate memory for root of this subtree  
##        # and increment constructTreeUtil.preIndex 
##        root = BinarySearchTreeMap.Node(key) 
##        index += 1 
##  
##        if(index < size): 
##             
##            # Construct the subtree under root  
##            # All nodes which are in range {min.. key} will 
##            # go in left subtree, and first such node will  
##            # be root of left subtree 
##            root.left = restore_bst_helper(pre, pre[index], mini, key, size) 
##  
##            # All nodes which are in range{key..max} will 
##            # go to right subtree, and first such node will 
##            # be root of right subtree 
##            root.right = restore_bst_helper(pre, pre[index], key, maxi, size) 
##  
##    return root
            

def main():
    x = restore_bst([9, 7, 3, 1, 5, 13, 11, 15])
    print(x.item.key)

main()
                
                
        
    
    
