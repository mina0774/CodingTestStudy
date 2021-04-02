# 3-way QuickSort

def sort(array,lo,hi):
    if hi<=lo:
        return
    lt=lo
    gt=hi

    pivot=array[lo]
    i=lo

    while i<=gt:
        if array[i]<pivot:
            array[lt],array[i]=array[i],array[lt]
            lt+=1
            i+=1
        elif array[i]>pivot:
            array[i],array[gt]=array[gt],array[i]
            gt-=1
        else:
            i+=1


    sort(array,lo,lt-1)
    sort(array,gt+1,hi)

array=[2,4,5,6,7,4,3,5,4,2,3,8,8,8,9]
sort(array,0,len(array)-1)
print(array)