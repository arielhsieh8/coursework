#hw2q7

def findChange(lst01):
    left = 0
    right = len(lst01)-1
    mid = (left+right)//2
    while left <= right:
        mid = (left+right)//2
        if lst01[mid] == 0:
            left = mid +1
        else:
            right = mid -1
    return left

def main():
    x = findChange([0,0,0,0,1,1,1,1])
    print(x)

    
