# 부품 찾기

################## 이진 탐색을 이용한 소스코드 #######################
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

def binary_search_solution():
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

################## 계수 정렬 이용한 소스코드 #######################
# 계수 정렬은 모든 원소의 번호를 포함할 수 있는 크기의 리스트를 생성 후,
# 리스트의 인덱스에 직접 접근하는 방
def counting_sort_solution():
    n=int(input())
    array=[0]*1000001

    # 가게에 있는 전체 부품을 입력받아 해당하는 부품 번호와 배열의 인덱스가 일치하는 부분에 값을 1로 지정
    for i in input().split():
        array[int(i)]=1

    m=int(input())
    guest_array=list(map(int,input().split()))

    for i in guest_array:
        if array[i]==1:
            print('yes', end=' ')
        else:
            print('no', end=' ')

################## 집합 자료형을 이용한 소스코드 #######################
def set_solution():
    n=int(input())
    array=set(map(int,input().split()))

    m=int(input())
    guest_array=list(map(int,input().split()))

    for i in guest_array:
        if i in array:
            print('yes', end=' ')
        else:
            print('no', end=' ')
set_solution()