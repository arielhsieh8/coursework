#hw6q3

from DoublyLinkedList import *

class CompactString():
    def __init__(self, orig_str):
        self.data = DoublyLinkedList()
        orig_str += " "
        temp = orig_str[0]
        count = 1
        for i in range(1,len(orig_str)):
            if orig_str[i] == temp:
                count += 1
            else:
                self.data.add_last(tuple([temp,count]))
                temp = orig_str[i]
                count = 1

    def __add__(self,other):
        new = CompactString("")
        if self.data.trailer.prev.data[0] == other.data.header.next.data[0]:
            let = self.data.trailer.prev.data[0]
            num = self.data.trailer.prev.data[1] + other.data.header.next.data[1]
            current = self.data.header.next
            while current != self.data.trailer.prev:
                new.data.add_last(current.data)
                current = current.next
        else:
            current = self.data.header.next
            while current != self.data.trailer:
                new.data.add_last(current.data)
                current = current.next
        #self
        if self.data.trailer.prev.data[0] == other.data.header.next.data[0]:
            new.data.add_last(tuple([let,num]))
            current = other.data.header.next.next
        else:
            current = other.data.header.next
        #other 
        while current != other.data.trailer:
            new.data.add_last(current.data)
            current = current.next
        return new


    def __lt__(self,other):
        curr_self = self.data.header.next
        curr_other = other.data.header.next
        while curr_self != self.data.trailer:
            if curr_other == other.data.trailer:
                return False 
            if curr_self.data[0] == curr_other.data[0]:
                if curr_self.data[1] > curr_other.data[1]:
                    if curr_self.next == self.data.trailer:
                        return False
                    else:
                        return True
                elif curr_self.data[1] == curr_other.data[1]:
                    if curr_self.next == self.data.trailer and curr_other.next == other.data.trailer:
                        temp = False
                    elif curr_self.next == self.data.trailer:
                        temp == True
                    elif curr_other.next == other.data.trailer:
                        temp = False
                    else:
                        temp = True
                else:
                    if curr_self.next == self.data.trailer:
                        return True
                    else: 
                        return False
            elif curr_self.data[0] < curr_other.data[0]:
                return True
            else:
                return False
            curr_self = curr_self.next
            curr_other = curr_other.next
        return temp

    def __le__(self,other):
        curr_self = self.data.header.next
        curr_other = other.data.header.next
        while curr_self != self.data.trailer:
            if curr_other == other.data.trailer:
                return False 
            if curr_self.data[0] == curr_other.data[0]:
                if curr_self.data[1] > curr_other.data[1]:
                    if curr_self.next == self.data.trailer:
                        return False
                    else:
                        return True
                elif curr_self.data[1] == curr_other.data[1]:
                    temp = True 
                else:
                    if curr_self.next == self.data.trailer:
                        return True
                    else: 
                        return False
            elif curr_self.data[0] < curr_other.data[0]:
                return True
            else:
                return False
            curr_self = curr_self.next
            curr_other = curr_other.next
        return temp


    def __gt__(self,other):
        curr_self = self.data.header.next
        curr_other = other.data.header.next
        while curr_self != self.data.trailer:
            if curr_other == other.data.trailer:
                return True 
            if curr_self.data[0] == curr_other.data[0]:
                if curr_self.data[1] < curr_other.data[1]:
                    if curr_self.next == self.data.trailer:
                        return False
                    else:
                        return True
                elif curr_self.data[1] == curr_other.data[1]:
                    if curr_self.next == self.data.trailer and curr_other.next == other.data.trailer:
                        temp = False
                    elif curr_self.next == self.data.trailer:
                        temp == False
                    elif curr_other.next == other.data.trailer:
                        temp = True
                    else:
                        temp = False
                else:
                    return False 
            elif curr_self.data[0] > curr_other.data[0]:
                return True
            else:
                return False
            curr_self = curr_self.next
            curr_other = curr_other.next
        return temp


    def __ge__(self,other):
        curr_self = self.data.header.next
        curr_other = other.data.header.next
        while curr_self != self.data.trailer:
            if curr_other == other.data.trailer:
                return True 
            if curr_self.data[0] == curr_other.data[0]:
                if curr_self.data[1] < curr_other.data[1]:
                    if curr_self.next == self.data.trailer:
                        return False
                    else:
                        return True
                elif curr_self.data[1] == curr_other.data[1]:
                    temp = True 
                else:
                    return False 
            elif curr_self.data[0] > curr_other.data[0]:
                return True
            else:
                return False
            curr_self = curr_self.next
            curr_other = curr_other.next
        return temp

            
    def __repr__(self):
        res_str = ""
        current = self.data.header.next
        while current != self.data.trailer:
            res_str += ((current.data[0])*current.data[1])
            current = current.next
        return res_str

def main():
    s1 = CompactString("aaaaaaacccaaaa")
    s2 = CompactString("aaaaabbbaaac")
    
    s3 = s2 + s1
    print(s1.data)
    print(s2.data)
    print(s3.data)
    #true/false
    print(s1>s2) #false
    #print(s3>=s1) #true
##    print(s1<=s3) #true
##    print(s3<=s1) #false
##    print(s1>s3)#false
##    print(s3>s1)#true
##    print(s1>=s3) #false
##    print(s3>=s1) #true
##    

#main()
            
        
