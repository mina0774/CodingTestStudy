class HashTable:
    def __init__(self,hash_func):
        self.hash_func=hash_func
        self.hash_table=[None]*3

    def set(self,key,value):
        hash=self.hash_func(key)
        self.hash_table[hash]=value

    def get(self,key):
        hash=self.hash_func(key)
        return self.hash_table[hash]

tb=HashTable(lambda x: ord(x)%3)
tb.set('a',0)
tb.set('b',1)
tb.set('c',2)
tb.set('d',3)

for key in ['a','b','c','d']:
    print(tb.get(key),end=' ')