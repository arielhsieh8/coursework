def fun1(n):
    if (n == 0):
        return 1
    else:
        part1 = fun1(n-1)
        part2 = fun1(n-1)
        res = part1 + part2
    return res
