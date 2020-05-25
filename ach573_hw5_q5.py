#hw6q5

from DoublyLinkedList import *

def merge_linked_lists(srt_lnk_lst1, srt_lnk_lst2):
    def merge_sublists(first_node,second_node,new_lst):
        if first_node is srt_lnk_lst1.trailer and second_node is srt_lnk_lst2.trailer:
            return new_lst
        else:
            if first_node is srt_lnk_lst1.trailer:
                new_lst.add_last(second_node.data)
                return merge_sublists(first_node,second_node.next,new_lst)
            elif second_node is srt_lnk_lst2.trailer:
                new_lst.add_last(first_node.data)
                return merge_sublists(first_node.next,second_node,new_lst)
            
            if first_node.data > second_node.data:
                new_lst.add_last(second_node.data)
                return merge_sublists(first_node,second_node.next,new_lst)
            elif first_node.data <= second_node.data:
                new_lst.add_last(first_node.data)
                return merge_sublists(first_node.next,second_node,new_lst)
            
    return merge_sublists(srt_lnk_lst1.header.next,srt_lnk_lst2.header.next,new_lst=DoublyLinkedList())


def main():
    lst1 = DoublyLinkedList()
    lst1.add_last(1)
    lst1.add_last(5)
    lst1.add_last(6)
    lst2 = DoublyLinkedList()
    lst2.add_last(2)
    lst2.add_last(3)
    lst2.add_last(7)
    x=merge_linked_lists(lst1,lst2)
    print(x)

#main() 
