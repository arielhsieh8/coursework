#hw5q1

from ArrayStack import *

def postfix_calc(input_str):
    s = ArrayStack() 
    lst = input_str.split(" ") 
    for i in range(len(lst)):
        if lst[i].isdigit():
            s.push(int(lst[i]))
        else: 
            num2 = s.pop()
            num1 = s.pop()
            if lst[i] == "+":
                res = num1 + num2
            elif lst[i] == "-":
                res = num1 - num2
            elif lst[i] == "*":
                res = num1 * num2
            elif lst[i] == "/":
                res = num1 / num2
            s.push(res)
    return s.pop()

input_str = input("--> ")
thisdict = {} 
while input_str != "done()":
    if len(input_str) != 1:
        if input_str[0].isalpha():
            if input_str[2] == "=":
                new_str1 = input_str[4:]
            else:
                new_str1 = input_str
                
            new_lst = new_str1.split(" ")
            for i in range(len(new_lst)):
                if new_lst[i] in thisdict.keys():
                    new_lst[i] = str(thisdict[new_lst[i]])
            new_str = " ".join(new_lst)
            x = postfix_calc(new_str)
            
            if input_str[2] == "=":
                thisdict[input_str[0]] = x
                print(input_str[0])
            else:
                print(x) 
        else:
            x = postfix_calc(input_str)
            print(x) 
    else:
        if input_str[0].isalpha():
            print(thisdict[input_str[0]])
        else:
            print(int(input_str))    
    input_str = input("--> ")

