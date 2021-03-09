import random

r=random.randint(0,5)
print(r)

for i in range(1000):
    r=random.randint(0,5)
    print(r)

my_counter=dict()

for i in range(1000):
    r=random.randint(0,4)
    if r in my_counter.keys():
        my_counter[r]=my_counter[r]+1
    else:
        my_counter[r]=1

print(my_counter)

# shuffling practice

# swap function
def swap(array,index_1,index_2):
    temp=array[index_1]
    array[index_1]=array[index_2]
    array[index_2]=temp



for _ in range(10):
    a=[1,2,3,4,5,6,7,8,9]
    for i in range(len(a)):
        r=random.randint(i,len(a)-1)
        swap(a,i,r)
    print(a)