import sys
# 입력되는 데이터 수가 많을 때, 이를 처리해주면 좀 더 입력을 빠르게 받을 수 있음
input=sys.stdin.readline
# 무한대 값을 10억으로 설정
INF=int(1e9)

# 노드의 개수, 간선의 개수를 입력 받음
n,m=map(int,input().split())
# 노드의 시작 번호를 입력 받기
start=int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph=[[] for i in range(n+1)]
# 방문한 적이 있는 체크하는 목적의 리스트
visited=[False] * (n+1)
# 최단 거리 저장 테이블 - 모두 무한대로 초기화
distance=[INF] * (n+1)

# 모든 간선 정보를 입력하기
for _ in range(m):
    # a번 노드 -> b번 노드로 가기 위한 비용 = c
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호를 반환
def get_smallest_node():
    min_value=INF
    # 가장 최단 거리가 짧은 노드 (인덱스)
    index = 0
    for i in range(1,n+1):
        if distance[i]<min_value and not visited[i]:
            min_value=distance[i]
            index=i
    return index

def dijkstra(start):
    # 시작 노드에 대해 초기화
    distance[start]=0
    visited[start]=True

    for j in graph[start]:
        distance[j[0]]=j[1]

    # 시작 노드를 제외한 전체 n-1개의 노드에 대해서 반복을 해줘야 함
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서 방문 처리
        now=get_smallest_node()
        visited[now]=True

        for j in graph[now]:
            cost=distance[now]+j[1]

            if cost<distance[j[0]]:
                distance[j[0]]=cost

dijkstra(start)

# 모든 노드에 대한 최단 거리 출력
for i in range(1,n+1):
    # 도달할 수 없는 경우 무한이라고 출력
    if distance[i]==INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])

