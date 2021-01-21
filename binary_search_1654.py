# 백준 - 랜선 자르기

# K는 오영식이 이미 가지고 있는 랜선 개수, N은 필요한 랜선의 개수
# K를 잘라서 N개 이상이 되도록 만들면 되고, 일정한 길이로 자를 수 있는 최대 랜선 길이를 구하는 문제임
k,n=map(int,input().split())

array=[]
for _ in range(k):
    array.append(int(input()))

# 이진 탐색을 이용하여 이 문제를 해결할 수 있음
# 먼저 오영식이 이미 가지고 있는 랜선들 중 가장 큰 길이의 랜선을 기준으로 시작점,끝점을 지정
start=1
end=max(array)

# 이진 탐색 시작
result=0
while (start<=end):
    # 총 랜선 개수를 저장할 변수
    total=0
    mid=(start+end)//2

    for i in array:
        total+=i//mid

    # 만약 잘려서 만들어진 총 랜선의 개수가 필요한 랜선의 개수보다 작다면
    # 더 작은 단위로 잘라야하므로 끝점을 다시 설정
    if total<n:
        end=mid-1
    # 만약 잘려서 만들어진 총 랜선의 개수가 필요한 랜선의 개수보다 크다면
    # 더 큰 단위로 잘라야하므로 끝점을 다시 설정
    # 현재 이 값이 답이 될 수도 있으니 result에 저장
    else:
        result=mid
        start=mid+1

print(result)



