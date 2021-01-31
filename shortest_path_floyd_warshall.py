# 플로이드 워셜 알고리즘
# 모든 지점에서 다른 모든 지점까지의 최단 경로를 모두 구하는 경우

INF=int(1e9)

# 노드 개수 입력 받기
n=int(input())
# 간선 개수 입력 받기
m=int(input())

# 2차원 리스트(그래프 표현)을 만든 후, 모든 값을 무한값으로 초기화
graph=[[INF]*(n+1) for _ in range(n+1)]

# 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

# 각 간선 정보를 입력받아, 그 값을 초기화
for _ in range(m):
    # a에서 b로 가는 비용은 c
    a,b,c=map(int,input().split())
    graph[a][b]=c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])

# 수행 결과 출력
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print("INFINITY",end=' ')
        else:
            print(graph[a][b],end=' ')
    print()
