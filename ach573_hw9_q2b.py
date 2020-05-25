#hw9q2b

from ChainingHashTableMap import * 


def intersection_list(lst1, lst2):
    hash_table = ChainingHashTableMap()
    lst3 = []
    for elem in lst1:
        hash_table[elem] = None
    for elem in lst2:
        if elem in hash_table:
            lst3.append(elem)
    return lst3

def main():
    lst1 = [4, 1, 8, 2]
    lst2 = [3, 9, 2, 7, 1]
    lst = intersection_list(lst1, lst2)
    print(lst)

#main()
                
