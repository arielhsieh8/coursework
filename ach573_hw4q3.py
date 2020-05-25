#hw4q3

def print_triangle(n):
    if n == 1:
        print("*"*n)
    else:
        print_triangle(n-1)
        print("*"*n)

def print_opposite_triangle(n):
    if n == 0:
        print("*"*n, end = "")
    else:
        print("*"*n)
        print_opposite_triangle(n-1)
        print("*"*n)

def print_ruler(n):
    if n == 1:
        print("-"*n)
    else:
        print_ruler(n-1)
        print("-"*n)
        print_ruler(n-1)
