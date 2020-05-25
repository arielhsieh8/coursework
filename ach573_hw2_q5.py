#hw2q5

def split_parity(lst):
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst.append(lst[i])
            lst.remove(lst[i])
    return lst

def main():
    x = split_parity([1,2,3,4,5,6,7,8])
    print(x)

