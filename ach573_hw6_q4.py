#hw6q4

from DoublyLinkedList import *

def copy_linked_list(lnk_lst):
    new_lnk_lst = DoublyLinkedList() 
    current = lnk_lst.header.next
    while current != lnk_lst.trailer:
        new_lnk_lst.add_last(current.data)
        current = current.next
    return new_lnk_lst

def deep_copy_linked_list(lnk_lst):
    new_lnk_lst = DoublyLinkedList()
    if not(isinstance(lnk_lst,DoublyLinkedList)):
        return lnk_lst
    else:
        for elem in lnk_lst:
            val = deep_copy_linked_list(elem)
            new_lnk_lst.add_last(val)
    return new_lnk_lst 
            

def main():
    lnk_lst1 = DoublyLinkedList()
    elem1 = DoublyLinkedList()
    elem1.add_last(1)
    elem1.add_last(2)
    lnk_lst1.add_last(elem1)
    elem2 = 3
    lnk_lst1.add_last(elem2)

    print(lnk_lst1)
    lnk_lst2 = deep_copy_linked_list(lnk_lst1)
    print(lnk_lst2)
    e1 = lnk_lst1.header.next
    e1_1 = e1.data.header.next
    e1_1.data = 10
    e2 = lnk_lst2.header.next
    e2_1 = e2.data.header.next
    print(e2_1.data)

#main()
