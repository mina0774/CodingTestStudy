# 미래도시 - 플로이드 워셜 알고리즘 이용
import sys
input=sys.stdin.readline

INF=int(1e9)

# 노드 수, 간선 수 입력 받기
n,m=map(int,input().split())
# 최단 경로 저장할 2차원 리스트 만들기
graph=[[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는 거리는 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

# 간선에 대한 정보 입력 받기
for _ in range(m):
    # a <-> b로 가는 비용은 1이라고 가정
    # 양방향 이동 가능
    a,b=map(int,input().split())
    graph[a][b]=1
    graph[b][a]=1

# x번 회사, k번 회사 입력 받기
x,k=map(int,input().split())

# 플로이드 워셜 알고리즘 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

distance=graph[1][k]+graph[k][x]

# 도달할 수 없는 경우 -1 출력
if distance>=INF:
    print("-1")
# 도달할 수 있다면 최단 거리 출력
else:
    print(distance)