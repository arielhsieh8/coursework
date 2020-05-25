#hw1q5

##alternate 
##def fibs(n):
##    x = 1
##    y = 1
##    for i in range(n):
##        yield x
##        x,y = y,x+y

def fibs(n):
    curr = 0
    lst = [0]
    nxt = 1
    while (curr < n):
        lst.append(nxt);
        yield nxt
        nxt = sum(lst)
        lst.pop(0);
        curr += 1;

def main():
    for curr in fibs(20):
        print(curr)

main()
