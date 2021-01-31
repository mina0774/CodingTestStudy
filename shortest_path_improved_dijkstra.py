# 개선된 다익스트라 알고리즘
# '최단 거리가 가장 짧은 노드'를 선택하는 과정을 다익스트라 최단 경로 함수 안에서 우선순위 큐를 이용하는 방식으로 대체하기 때문에
# 최단 거리를 구하는 get_smallest_node가 필요없음

import heapq
import sys
input=sys.stdin.readline
# 무한을 의미하는 값을 10억으로 설정
INF=int(1e9)

# 노드의 개수, 간선의 개수 입력 받기
n,m=map(int,input().split())
# 시작 노드 입력 받기
start=int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트
graph=[[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance=[INF]*(n+1)

# 모든 간선 정보 입력 받기
for _ in range(m):
    # a노드 -> b노드로 이동하는 비용 => c
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    # 시작노드로 가기 위한 최단 경로를 으로 설정, 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start]=0

    # q가 비어있지 않을 때까지 반복
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼냄
        dist,now=heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now]<dist:
            continue

        # 현재 노드와 연결된 다른 인접 노드 확인
        for i in graph[now]:
            cost=dist+i[1]
            # 현재 노드를 거쳐, 다른 노드로 이동하는 거리가 더 짧은 경우에
            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INFINITY")
    else:
        print(distance[i])
