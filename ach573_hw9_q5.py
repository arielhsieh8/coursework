#hw9q5

from ChainingHashTableMap import *

class InvertedFile: #need to change the words to numbers so you can hash it 
    def __init__(self, filename):
        new_line = ""
        file = open(filename,"r")
        big_list = []
        for line in file:
            for char in line:
                if char.isalpha() or char == " ":
                    new_line += char       
            new_line += " "
        big_list = new_line.split(" ")
        res_lst = [] 
        for elem in big_list:
            if elem != "":
                res_lst.append(elem)
        file.close() 
                
        self.table = ChainingHashTableMap()
        for i in range(len(res_lst)):
            key = res_lst[i].lower() #need to deal with punctuation
            if key in self.table:
                lst = self.table[key]
                lst.append(i) 
            else:
                lst = [i] 
            self.table[key] = lst        

    def indices(self, word):
        if word.lower() in self.table:
            return self.table[word.lower()]
        else:
            return []


def main():
    D = ["row", "row", "row", "your", "boat", "gently", "down",
         "the", "stream"]
    x = InvertedFile("row your boat.txt")
    l = x.indices("row")
    print(l)

#main()
            
        
            

            
        
            
