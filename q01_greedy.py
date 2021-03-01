# 그리디 문제 - 모험가 길드 (복습)
# 공포도를 오름차순으로 정렬하면, 항상 최소한의 모험가의 수만 포함하여 그룹을 결성하게 되므로
# 최대한 많은 그룹이 구성되는 방법이므로 항상 최적의 해를 찾을 수 있음

n=int(input())
array=list(map(int,input().split()))
array.sort()

count=0
result=0
for a in array:
    count+=1

    # 현재 그룹에 포함된 사람 수가 현재 공포도 이상이라면 그룹 결성
    if count>=a:
        result+=1
        count=0

print(result)