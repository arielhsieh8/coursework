import random
from UnsortedArrayMap import UnsortedArrayMap

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
        self.table = [None for i in range(self.N)]
        self.n = 0
        self.hash_function = ChainingHashTableMap.MADHashFunction(N)

    def __len__(self):
        return self.n

    def is_empty(self):
        return (len(self) == 0)

    def __getitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if isinstance(curr_bucket, UnsortedArrayMap):
            return curr_bucket[key]
        elif isinstance(curr_bucket, UnsortedArrayMap.Item):
            return curr_bucket.value

    def __setitem__(self, key, value):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if isinstance(curr_bucket, UnsortedArrayMap):
            old_size = len(curr_bucket)
            curr_bucket[key] = value
            new_size = len(curr_bucket)
            if (new_size > old_size):
                self.n += 1
            if (self.n > self.N):
                self.rehash(2 * self.N)
        elif isinstance(curr_bucket, UnsortedArrayMap.Item):
            keyz = curr_bucket.key
            val = curr_bucket.value
            self.table[i] = UnsortedArrayMap()
            curr_bucket = self.table[i] 
            curr_bucket[keyz] = val
            
            old_size = len(curr_bucket)
            curr_bucket[key] = value
            new_size = len(curr_bucket)
            if (new_size > old_size):
                self.n += 1
            if (self.n > self.N):
                self.rehash(2 * self.N)
        else:
            self.table[i] = UnsortedArrayMap.Item(key, value)
            self.n += 1 

    def __delitem__(self, key):
        i = self.hash_function(key)
        curr_bucket = self.table[i]
        if isinstance(curr_bucket, UnsortedArrayMap):
            del curr_bucket[key]
            self.n -= 1
            if len(self.table[i]) == 1:
                for key in self.table[i]:
                    keyz = key 
                    val = curr_bucket[key] 
                self.table[i] = UnsortedArrayMap.Item(keyz, val)
            if (self.n < self.N // 4):
                self.rehash(self.N // 2)
        elif isinstance(curr_bucket, UnsortedArrayMap.Item):
            self.table[i] = None
            self.n -= 1
            if (self.n < self.N // 4):
                self.rehash(self.N // 2)
        else:
            raise KeyError("No key: " + str(key) + " found")

    def __iter__(self):
        for curr_bucket in self.table:
            if isinstance(curr_bucket, UnsortedArrayMap): 
                for key in curr_bucket:
                    yield key
            elif isinstance(curr_bucket, UnsortedArrayMap.Item):
                yield curr_bucket.key

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
        if isinstance(curr_bucket, UnsortedArrayMap): 
            for key in curr_bucket:
                print("(", key, ", ", curr_bucket[key], ")", sep="", end=" ")
            print()
        elif isinstance(curr_bucket, UnsortedArrayMap.Item):
            print("(", curr_bucket.key, ", ", curr_bucket.value, ")", sep="", end="")
            print()
        else:
            print("None")

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
    #print_hash_table(ht)
##    del ht[1]
##    del ht[3]
##    del ht[7]
##    del ht[4]
##    del ht[2]
##    del ht[11]
##    del ht[10]
    #del ht[12]
##    del ht[22]
##    del ht[106]
##    del ht[36]
##    del ht[72]
##    del ht[902]
##    del ht[86]
##    del ht[96]
##    del ht[62]
    #del ht[42]
    print_hash_table(ht)
    #print(ht.table.key)

#main()
