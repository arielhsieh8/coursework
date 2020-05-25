#hw1q2

def shift(lst, k, direction):
    if direction == "left":
        for i in range(k):
            removed = lst.pop(0)
            lst.append(removed)
    else:
        for i in range(k):
            removed = lst.pop()
            lst.insert(0,removed)
    return lst


def main():
    x = shift([1,2,3,4,5,6],3,"right")
    print(x);


