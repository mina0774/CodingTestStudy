# 이진 탐색
# 정렬된 배열에서 특정 수의 개수 구하기
# bisect 이용하기
'''
bisect_left(a,x) - 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
bisect_right(a,x) - 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
'''

from bisect import bisect_left,bisect_right

def count_by_value(array,left_value,right_value):
    right_index=bisect_right(array,right_value)
    left_index=bisect_left(array,left_value)

    return right_index-left_index

n,x=map(int,input().split())
array=list(map(int,input().split()))

count=count_by_value(array,x,x)

if count==0:
    print(-1)
else:
    print(count)