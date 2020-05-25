#hw4q7

def split_by_sign(lst, low, high):
    if low == high:
        return lst
    else:
        if lst[low] > 0:
            if lst[high] < 0:
                lst[low],lst[high] = lst[high],lst[low]
                return split_by_sign(lst,low+1,high)
            else:
                return split_by_sign(lst,low,high-1)
        else:
            return split_by_sign(lst,low+1,high) 

    
