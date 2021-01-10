n=map(int,input())
fear_list=[]
fear_list=list(map(int,input().split()))

fear_list.sort()

result=0 # 총 그룹의 수
count=0 # 현재 그룹에 포함된 모험가의 수

# 오름차순으로 정의된 모험가 수를 공포도가 낮은 것부터 하나씩 확인함
for i in fear_list:
    count+=1 # 현재 그룹에 해당 모험가를 포함시키고

    # 현재 그룹의 모험가 수가 현재 모험가의 공포도 이상이면
    if i<=count:
        result+=1
        count=0

print(result)
