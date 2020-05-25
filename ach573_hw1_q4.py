#hw1q4

def tens():
    lst = [10**i for i in range(6)]
    return lst

def second():
    lst = [(i+1)*i for i in range(10)]
    return lst

def third():
    lst = [chr(i) for i in range(97,123)]
    return lst 

def main():
    x = tens();
    print(x)




    
