#hw6q2

from DoublyLinkedList import *

class Integer():
    def __init__(self,num_str):
        self.data = DoublyLinkedList()
        for char in num_str:
            self.data.add_last(char)

    def __add__(self,item):
        new_num_str = ""
        carry = 0
        curr_self = self.data.trailer.prev
        curr_item = item.data.trailer.prev
        if len(self.data) >= len(item.data):
            while curr_self != self.data.header:
                if curr_item == item.data.header:
                    other_num = "0"
                else:
                    other_num = curr_item.data
                self_num = curr_self.data
                result = int(self_num) + int(other_num)
                result += carry 
                if result > 9:
                    result = result - 10
                    carry = 1
                else:
                    carry = 0
                new_num_str += str(result)
                if curr_item != item.data.header: 
                    curr_item = curr_item.prev
                curr_self = curr_self.prev
                if curr_self == self.data.header and carry == 1:
                    new_num_str += str(carry)
        else:
            while curr_item != item.data.header:
                if curr_self == self.data.header:
                    self_num = "0"
                else:
                    self_num = curr_self.data
                other_num = curr_item.data
                result = int(self_num) + int(other_num)
                result += carry
                if result > 9:
                    result = result - 10
                    carry = 1
                else:
                    carry = 0
                new_num_str += str(result)
                if curr_self != self.data.header:
                    curr_self = curr_self.prev
                curr_item = curr_item.prev
                if curr_item == item.data.header and carry == 1:
                    new_num_str += str(carry)
        new_num_str = new_num_str[::-1]
        i = 0
        while new_num_str[i] == "0":
            new_num_str = new_num_str[i+1:]
            i+=1 
        sum_int = Integer(new_num_str)
        return sum_int 
        
    def __mul__(self,other):
        new_num_str = ""
        num_str = ""
        temp_lst = []
        final_res = 0
        carry = 0
        count = 0
        if len(self.data) >= len(other.data):
            curr_first = self.data.trailer.prev
            curr_second = other.data.trailer.prev
            while curr_second != other.data.header:
                while curr_first != self.data.header:
                    num1 = int(curr_first.data)
                    num2 = int(curr_second.data)
                    mul_res = num1*num2 + carry 
                    if mul_res > 9 and curr_first.prev != self.data.header:
                        carry = mul_res//10
                        mul_res = mul_res%10
                    else:
                        carry = 0
                    if mul_res > 9:
                        mul_res_str = str(mul_res)
                        mul_res_str = mul_res_str[::-1]
                        num_str += mul_res_str
                    else:
                        num_str += str(mul_res)
                    curr_first = curr_first.prev
                num_str = num_str[::-1] + ("0"*count)
                temp_lst.append(num_str)
                count += 1
                curr_second = curr_second.prev
                curr_first = self.data.trailer.prev
                num_str = ""
        else:
            curr_first = other.data.trailer.prev
            curr_second = self.data.trailer.prev
            while curr_second != self.data.header:
                while curr_first != other.data.header:
                    num1 = int(curr_first.data)
                    num2 = int(curr_second.data)
                    mul_res = num1*num2 + carry 
                    if mul_res > 9 and curr_first.prev != other.data.header:
                        carry = mul_res//10
                        mul_res = mul_res%10
                    else:
                        carry = 0
                    if mul_res > 9:
                        mul_res_str = str(mul_res)
                        mul_res_str = mul_res_str[::-1]
                        num_str += mul_res_str
                    else:
                        num_str += str(mul_res)
                    curr_first = curr_first.prev
                num_str = num_str[::-1] + ("0"*count)
                temp_lst.append(num_str)
                count += 1
                curr_second = curr_second.prev
                curr_first = other.data.trailer.prev
                num_str = ""
        
        for elem in temp_lst:
            final_res += int(elem)
        new_num = str(final_res)
        mul_int = Integer(new_num)
        return mul_int
            

    def __repr__(self):
        res_str = ""
        current = self.data.header.next
        while current != self.data.trailer:
            res_str += current.data
            current = current.next
        return res_str

def main():
    n1 = Integer("54")
    n2 = Integer("235")
    #c = Integer()
    print(n1)
    print(n2)
    n3 = n1 * n2
    print(n3)
    #print(c)

#main() 

