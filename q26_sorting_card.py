# 정렬 - 카드 정렬하기 (백준 1715)

# 항상 작은 크기의 두 카드 묶음을 합쳤을 때 최적의 해를 보장
# 우선순위 큐를 이용하면 되겠네
import heapq

n=int(input())

heap=[]
for i in range(n):
    data=int(input())
    heapq.heappush(heap,data)

result=0

# 힙에 원소가 1개 남을 때까지 반복
while len(heap)!=1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    one=heapq.heappop(heap)
    two=heapq.heappop(heap)

    sum_value=one+two

    result+=sum_value
    heapq.heappush(heap,sum_value)

print(result)