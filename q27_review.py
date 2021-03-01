# 이진탐색
# 정렬된 배열에서 특정 수의 개수 구하기

n,x=map(int,input().split())

array=list(map(int,input().split()))

def count_by_value(array,x):

    n=len(array)

    start_index=first(array,x,0,n-1)

    if start_index==None:
        return -1

    last_index=last(array,x,0,n-1)

    return last_index-start_index+1


def first(array,x,start,end):
    if start>end:
        return None

    mid=(start+end)//2

    if (mid==0 or array[mid-1]<x) and array[mid]==x:
        return mid
    elif array[mid]>=x:
        return first(array,x,start,mid-1)
    else:
        return first(array,x,mid+1,end)

def last(array,x,start,end):
    if start>end:
        return None

    mid=(start+end)//2

    if (mid==n-1 or array[mid+1]>x) and array[mid]==x:
        return mid
    elif array[mid]<=x:
        return last(array,x,mid+1,end)
    else:
        return last(array,x,start,mid-1)

print(count_by_value(array,x))