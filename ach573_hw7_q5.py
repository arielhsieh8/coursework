#hw7q5

from LinkedBinaryTree import *

def create_expression_tree(prefix_exp_str):
    expression_lst = prefix_exp_str.split()
    def create_expression_tree_helper(prefix_exp, start_pos):
        operator = ["+","-","*","/"]
        if prefix_exp[start_pos] not in operator:
            return (LinkedBinaryTree.Node(int(prefix_exp[start_pos])), start_pos)
        else:
            left_subtree = create_expression_tree_helper(prefix_exp, start_pos+1)
            right_subtree = create_expression_tree_helper(prefix_exp, left_subtree[1]+1)
            return (LinkedBinaryTree.Node(prefix_exp[start_pos],left_subtree[0],right_subtree[0]), right_subtree[1])

    return LinkedBinaryTree(create_expression_tree_helper(expression_lst,0)[0])

def prefix_to_postfix(prefix_exp_str):
    lst = []
    tree = create_expression_tree(prefix_exp_str)
    for elem in tree.postorder():
        if isinstance(elem.data, int):
            elem.data = str(elem.data)
        lst.append(elem.data)
    post_exp_str = " ".join(lst)
    return post_exp_str
                        

def main():
    exp_str = '+ / 4 - * 6 + 2 5 7 1'
    x = create_expression_tree(exp_str)
    for elem in x.preorder():
        print(elem.data)
    y = prefix_to_postfix(exp_str)
    print(y)

 #main()
        
            
                    
