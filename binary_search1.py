# 부품 찾기
def binary_search(target,array,start,end):
    while start<=end:
        mid=(start+end)//2

        if array[mid]==target:
            return mid
        elif array[mid]>target:
            end=mid-1
        else:
            start=mid+1
    return None

# N(가게의 부품 개수) 입력
n=int(input())
# 가게에 있는 부품의 번호를 공백으로 구분하여 입력
array=list(map(int,input().split()))
# 이진 탐색을 위해 가게에 있는 부품을 정렬
array.sort()

# M(손님이 확인 요청한 부품 개수) 입력
m=int(input())
# 손님이 확인 요청한 부품의 번호를 공백을 구분하여 입력
guest_array=list(map(int,input().split()))

# 손님이 확인 요청한 부품을 하나씩 확인
for i in guest_array:
    result=binary_search(i,array,0,n-1)

    if result==None:
        print('no',end=' ')
    else:
        print('yes',end=' ')