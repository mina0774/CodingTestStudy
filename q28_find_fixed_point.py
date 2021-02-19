# 이진탐색 고정점 찾기
# O(log N)으로 해결해야하므로 선형탐색이 아닌 이진탐색을 이용해야함

def binary_search(array,start,end):
    if start>end:
        return None

    mid=(start+end)//2

    if array[mid]==mid:
        return mid
    elif array[mid]>mid:
        return binary_search(array,start,mid-1)
    else:
        return binary_search(array,mid+1,end)

n=int(input())
array=list(map(int,input().split()))

# 이진탐색 수행
fixed_point=binary_search(array,0,n-1)

if fixed_point==None:
    print(-1)
else:
    print(fixed_point)