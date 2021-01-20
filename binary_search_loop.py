# 반복문을 이용하여 구현한 이진 탐색
def binary_search(array,target,start,end):
    while start<=end:
        mid=(start+end)//2

        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

n,target=map(int,input().split())
array=list(map(int,input().split()))

result=binary_search(array,target,0,n-1)
esult=binary_search(array,target,0,n-1)
if result==None:
    print("원소 X")
else:
    print(result+1)