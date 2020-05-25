#hw2q3
import math 

def factors(num):
    i = 1
    lst = []
    while i <= math.sqrt(num): 
        if num % i == 0:
            yield i
            if num // i != i:
                lst.append(num//i) 
        i += 1
    for j in range(-1,-len(lst)-1,-1):
        yield lst[j] 

def main():
    for curr_factor in factors(100):
        print(curr_factor)

        
        
