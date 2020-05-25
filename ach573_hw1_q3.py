#hw1q3

def squareSum(n):
    num = 0
    for i in range(n):
        num += i**2
    return num

def squareSum1(n):
    num = [i**2 for i in range(n)]
    return sum(num)

def oddSquareSum(n):
    num = 0
    for i in range(n):
        if i%2 != 0:
            num += i**2
    return num

def oddSquareSum1(n):
    num = [i**2 for i in range(n) if i%2 != 0]
    return sum(num) 

def main():
    x = squareSum(10)
    print(x)

 
