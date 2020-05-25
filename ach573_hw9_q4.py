#hw9q4

import random
from UnsortedArrayMap import UnsortedArrayMap

import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayQueue:
    INITIAL_CAPACITY = 8

    def __init__(self):
        self.data_arr = make_array(ArrayQueue.INITIAL_CAPACITY)
        self.n = 0
        self.front_ind = None

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def enqueue(self, item):
        if(self.n == len(self.data_arr)):
            self.resize(2 * len(self.data_arr))
        if(self.is_empty()):
            self.data_arr[0] = item
            self.front_ind = 0
            self.n = 1
        else:
            back_ind = (self.front_ind + self.n) % len(self.data_arr)
            self.data_arr[back_ind] = item
            self.n += 1

    def dequeue(self):
        if (self.is_empty()):
            raise Exception("Queue is empty")
        value = self.data_arr[self.front_ind]
        self.data_arr[self.front_ind] = None
        self.front_ind = (self.front_ind + 1) % len(self.data_arr)
        self.n -= 1
        if(self.n == 0):
            self.front_ind = None
        if((self.n < len(self.data_arr) // 4) and  (len(self.data_arr) > ArrayQueue.INITIAL_CAPACITY)):
            self.resize(len(self.data_arr) // 2)
        return value

    def first(self):
        if(self.is_empty()):
            raise Exception("Queue is empty")
        return self.data_arr[self.front_ind]

    def resize(self, new_size):
        old_data = self.data_arr
        new_data = make_array(new_size)
        old_ind = self.front_ind
        for new_ind in range(self.n):
            new_data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.data_arr = new_data
        self.front_ind = 0

class ChainingHashTableMap:
    class MADHashFunction:
        def __init__(self, N, p=40206835204840513073):
            self.N = N
            self.p = p
            self.a = random.randrange(1, self.p - 1)
            self.b = random.randrange(0, self.p - 1)

        def __call__(self, key):
            return ((self.a * hash(key) + self.b) % self.p) % self.N


    def __init__(self, N=64):
        self.N = N
        self.table = [UnsortedArrayMap() for i in range(self.N)]
        self.n = 0
        self.hash_function = ChainingHashTableMap.MADHashFunction(N)
        self.queue = ArrayQueue()

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        return curr_bucket[key]

    def __setitem__(self, key, value):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        old_size = len(curr_bucket)
        curr_bucket[key] = value
        new_size = len(curr_bucket)
        if (new_size > old_size):
            self.queue.enqueue(key)
            self.n += 1
        if (self.n > self.N):
            self.rehash(2 * self.N)

    def __delitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        del curr_bucket[key]
        self.queue.enqueue(key)  
        self.n -= 1
        if (self.n < self.N // 4):
            self.rehash(self.N // 2)

    def __iter__(self):
        lst = []
        while not(self.queue.is_empty()):
            key = self.queue.dequeue()
            if key in self:
                yield key
                lst.append(key)
        for elem in lst:
            self.queue.enqueue(elem) 

    def __contains__(self, key):
        try:
            val = self[key]
            return True
        except KeyError:
            return False

    def rehash(self, new_size):
        old = [(key, self[key]) for key in self]
        self.__init__(new_size)
        for (key, val) in old:
            self[key] = val


def print_hash_table(ht):
    for i in range(ht.N):
        print(i, ": ", sep="", end="")
        curr_bucket = ht.table[i]
        for key in curr_bucket:
            print("(", key, ", ", curr_bucket[key], ")", sep="", end=" ")
        print()

def main():
    ht = ChainingHashTableMap()
    ht[1] = None
    ht[2] = None
    ht[3] = None
    ht[4] = None
    ht[5] = None
    ht[6] = None
    ht[7] = None
    ht[8] = None
    ht[9] = None
    ht[10] = None
    ht[11] = None
    ht[1] = "hi"
    del ht[1]
    ht[10] = "bye"
    del ht[3]
    del ht[2]
    del ht[8]
    ht[9] = "cs"
    del ht[7]
    del ht[11]
    del ht[4]
    del ht[6] 
    print_hash_table(ht)
    for elem in ht:
        print(elem)

#main()

