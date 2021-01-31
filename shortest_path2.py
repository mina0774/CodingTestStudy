# 전보
# n,m의 범위가 크기 때문에 우선순위 큐를 이용한 다익스트라 알고리즘을 이용하여 문제를 해결할 수 있음

import heapq
import sys

input=sys.stdin.readline
INF=int(1e9)
# 노드수, 간선수, 시작노드 번호
n,m,c=map(int,input().split())

# 각 노드에 연결되어 있는 노드 정보를 담는 리스트
graph=[[] for i in range(n+1)]
# 최단 거리를 저장
distance=[INF]*(n+1)

# 모든 간선 정보 입력 받아 그래프에 저장
for _ in range(m):
    x,y,z=map(int,input().split())
    graph[x].append((y,z))

def dijkstra(start):
    q=[]
    # 시작노드로 가기 위한 최단경로를 0으로 설정하여 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        # 가장 최단 거리가 짧은 노드 정보 꺼냄
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue

        for i in graph[now]:
            cost=dist+i[1]
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(c)

# 도달할 수 있는 노드의 개수
count=0
# 도달할 수 있는 노드 중, 가장 멀리있는 노드
max_distance=0

for i in distance:
    if i!=INF:
        count+=1
        max_distance=max(max_distance,i)

# 시작노드는 제외하고 출력해야하므로 -1
print(count-1,max_distance)