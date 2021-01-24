# 효율적인 화폐 구성

# 이건 너무 어려워~ 복습이 필요해~
# 일단 화폐 단위가 배수가 아니므로 그리디 알고리즘은 못써
# 그래서 다이나믹 프로그래밍을 써야함
# 금액 i를 만들 수 있는 최소한의 화폐 개수를 Ai라고 할 때, 화폐 단위가 k라면
# Ai-k를 만드는 방법이 존재하는 경우엔 Ai=min(Ai,Ai-k+1)
# Ai-k를 만드는 방법이 존재하지 않는 경우엔 Ai=10001
# 이를 이용해서 리스트를 만들어보자

# 일단 첫째줄에 N,M을 입력으로 받아줘!
n,m=map(int,input().split())
array=[]
# N개의 화폐 단위 정보를 입력받기
for _ in range(n):
    array.append(int(input()))

d=[10001]*(m+1)

# 다이나믹 프로그래밍 진행 (보텀업)
d[0]=0
for i in range(n):
    for j in range(array[i],m+1):
        if d[j-array[i]]!=10001:
            d[j]=min(d[j],d[j-array[i]]+1)

if d[m]==10001:
    print(-1)
else:
    print(d[m])
