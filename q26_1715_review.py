# 카드 정렬하기 (백준 1715)
# 우선순위 큐를 이용

import heapq

n = int(input())

q=[]
for _ in range(n):
    heapq.heappush(q,int(input()))


result=0
while len(q)!=1:
    a=heapq.heappop(q)
    b=heapq.heappop(q)
    sum_value=a+b

    result+=sum_value
    heapq.heappush(q,sum_value)

print(result)


