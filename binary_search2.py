# 떡볶이 떡 만들기
# 절단기의 높이가 10억이니까 -> 너무 큰 수 -> 이진 탐색 써야겠네!
# N은 떡의 개수, M은 요청한 떡의 길이
n,m=map(int,input().split())
# 떡의 개별 높이
array=list(map(int,input().split()))

# 이진 탐색을 위한 시작점, 끝점 설정
start=0
end=max(array)

# 이진 탐색 수행
result=0
while(start<=end):
    total=0
    mid=(start+end)//2

    for i in array:
        if i>mid:
            total+=i-mid

    # 잘린 떡의 무게가 요구한 무게에 미치지 못할 경우
    # 떡을 더 잘라야하므로 끝점을 옮겨줌
    if total<m:
        end=mid-1
    # 잘린 떡의 무게가 요구한 무게에 충분할 경우
    # 떡을 덜 잘라야할수도 있고, 끝날수도 있으니까
    # result에 mid값을 넣어주고
    # 시작점을 옮겨줌
    else:
        result=mid
        start=mid+1

print(result)
