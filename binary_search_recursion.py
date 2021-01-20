# 재귀 함수를 이용한 이진 탐색 소스코드 구현
def binary_search(array,target,start,end):
    if start>end:
        return None

    mid=(start+end)//2

    if array[mid]==target:
        return mid
    elif array[mid]>target:
        return binary_search(array,target,start,mid-1)
    else:
        return binary_search(array,target,mid+1,end)

# n(원소 개수)과 target(찾고자 하는 문자열) 입력 받기
n,target=map(int,input().split())
# 전체 원소를 입력 받기
array=list(map(int,input().split()))

result=binary_search(array,target,0,n-1)
if result==None:
    print("원소 X")
else:
    print(result+1)

