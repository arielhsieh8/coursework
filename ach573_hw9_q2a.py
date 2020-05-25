#hw9q2

from ChainingHashTableMap import * 

def intersection_list(lst1, lst2):
    lst1.sort()
    lst2.sort()
    pointer1 = 0
    pointer2 = 0
    res_lst = []
    while pointer2 != len(lst2) and pointer1 != len(lst1):
        if lst1[pointer1] == lst2[pointer2]:
            res_lst.append(lst1[pointer1])
            pointer1 += 1
            pointer2 += 1
        elif lst1[pointer1] > lst2[pointer2]:
            pointer2 += 1
        else:
            pointer1 += 1
    return res_lst


def main():
    lst1 = [4, 1, 8, 2]
    lst2 = [3, 9, 2, 7, 1]
    lst = intersection_list(lst1, lst2)
    print(lst)

#main()
                
