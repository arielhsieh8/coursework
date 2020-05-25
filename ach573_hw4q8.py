#hw4q8

def flat_list(nested_lst, low, high):
    if low > high:
        return [] 
    else:
        if isinstance(nested_lst[low],list): 
            return flat_list(nested_lst[low],0,len(nested_lst[low])-1) + flat_list(nested_lst,low+1,high)
        else:
            return [nested_lst[low]] + flat_list(nested_lst,low+1,high)
