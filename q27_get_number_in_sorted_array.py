# 이진탐색
# 정렬된 배열에서 특정 수의 개수 구하기

# 정렬된 수열에서 값이 x인 원소를 세는 함수
def count_by_value(array,x):
    # 데이터의 개수
    n=len(array)

    # x가 처음 등장한 인덱스
    a=first(array,x,0,n-1)

    # 수열에 x가 존재하지 않는 경우
    if a==None:
        # x의 개수가 0이므로 0 반환
        return 0

    # x가 마지막으로 등장한 인덱스
    b=last(array,x,0,n-1)

    # 개수 반환
    return b-a+1

# 처음 위치를 찾는 이진 탐색 함수
def first(array,x,start,end):
    if start>end:
        return None

    mid=(start+end)//2

    if (mid==0 or x>array[mid-1]) and array[mid]==x:
        return mid
    elif array[mid]>=x:
        return first(array,x,start,mid-1)
    else:
        return first(array,x,mid+1,end)

# 마지막 위치를 찾는 이진 탐색 함수
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


n,x=map(int,input().split())
array=list(map(int,input().split()))

count=count_by_value(array,x)

if count==0:
    print(-1)
else:
    print(count)