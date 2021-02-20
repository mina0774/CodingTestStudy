# 이진탐색 -> 공유기 설치 (백준 2110)
# 집의 개수 - N / 공유기의 개수 - C
n,c=map(int,input().split())

# 전체 집의 좌표 정보 입력 받기
array=[]
for _ in range(n):
    array.append(int(input()))
# 이진 탐색 수행을 위해 정렬 수
array.sort()

start=1
end=array[-1]-array[0]

while start<=end:
    mid=(start+end)//2
    idx=0
    count=1

    for i in range(n):
        if array[i]>=array[idx]+mid:
            idx=i
            count+=1

    if count>=c:
        start=mid+1
        result=mid
    else:
        end=mid-1

print(result)


