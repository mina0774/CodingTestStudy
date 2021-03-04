# 최단 경로 문제 - 숨바꼭질 (다익스트라 - 특정 지점에서 모든 지점까지의 최단거리 구하기)
# 다익스트라는 bfs인데, 우선순위 큐를 이용함 (heapq 이용)

# 1-N까지의 헛간에 동빈이가 골라 숨을 수 있음
# 술래는 항상 1번 헛간에서 출발
# 전체 맵에 총 M개의 양방향 통로 존재, 하나의 통로는 두 헛간을 연결

# 동빈이는 1번 헛간으로부터 최단거리가 가장 먼 헛간이 가장 안전하다고 판단
# 동빈이가 숨을 헛간의 번호를 출력하는 프로그램 작성

# 출력) 첫번째는 숨어야하는 헛간 번호 (거리가 같은 헛간이 여러 개면, 가장 작은 헛간 번호 출력) / 헛간 까지의 거리 / 그 헛간과 같은 거리를 갖는 헛간의 개

import heapq

INF=int(1e9)
n,m=map(int,input().split())

# 출발 노드는 1번 노드
start = 1

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph=[[] for i in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance=[INF]*(n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append((b,1))
    graph[b].append((a,1))

def dijkstra(start):
    q=[]
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여 큐에 삽입
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist,now=heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접 노드들 확인
        for i in graph[now]:
            cost=i[1]+dist

            if cost<distance[i[0]]:
                distance[i[0]]=cost
                heapq.heappush(q,(cost,i[0]))

# 다익스트라 알고리즘 수행
dijkstra(start)

# 최단 거리가 가장 먼 노드 번호 (동빈이가 숨을 헛간의 번호)
max_node=0
# 최단 거리가 가장 먼 노드와의 이동 거리
res_distance=0
# 최단 거리가 가장 먼 노드와 동일한 최단 거리를 가지는 노드들의 리스트
result=[]
for i in range(1,n+1):
    if res_distance < distance[i]:
        max_node=i
        res_distance=distance[i]
        result=[max_node]
    elif res_distance==distance[i]:
        result.append(i)
print(max_node,res_distance,len(result))
