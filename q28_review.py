# 이진탐색 - 고정점 찾기

n=int(input())

array=list(map(int,input().split()))

def binary_search(array,start,end):
    if start>end:
        return -1
    mid=(start+end)//2

    if array[mid]==mid:
        return mid
    elif array[mid]>mid:
        end=mid-1
        return binary_search(array,start,end)
    else:
        start=mid+1
        return binary_search(array,start,end)

print(binary_search(array,0,n-1))
