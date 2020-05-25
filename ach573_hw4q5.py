#hw4q5

def count_lowercase(s, low, high):
    if low == high:
        if s[low] >= "a" and s[low] <= "z":
            count = 1
        else: 
            count = 0
        return count 
    else:
        if s[low] >= "a" and s[low] <= "z":
            return 1 + count_lowercase(s,low+1,high)
        else:
            return count_lowercase(s,low+1,high)

def is_number_of_lowercase_even(s,low,high):
    if low == high:
        if s[low] >= "a" and s[low] <= "z":
            return False
        else: 
            return True
    else:
        if s[low] >= "a" and s[low] <= "z":
            return not(is_number_of_lowercase_even(s,low+1,high))
        else:
            return is_number_of_lowercase_even(s,low+1,high)
        
