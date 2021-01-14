array=[5,7,9,0,3,1,6,2,4,8]

def quick_sort(array,start,end):
    # 원소의 개수가 1개인 경우 종료
    if start>=end:
        return
    # 피벗은 첫번째 원소
    pivot=start

    left=start+1
    right=end

    # left, right가 엇갈리지 않을 때까지 반복
    while left<=right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left<=end and array[left]<=array[pivot]:
            left+=1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right>=start+1 and array[right]>=array[pivot]:
            right-=1

        # 엇갈렸다면 작은 데이터와 피벗을 교체
        if left>right:
            array[right],array[pivot]=array[pivot],array[right]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            array[right],array[left]=array[left],array[right]

    # 분할 이후에 왼쪽 부분, 오른쪽 부분은 재귀 함수를 이용하여 다시 정렬을 수행
    quick_sort(array,start,right-1)
    quick_sort(array,right+1,end)

quick_sort(array,0,len(array)-1)
print(array)