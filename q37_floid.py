# 최단 경로 문제
# 플로이드 - 백준 11404
# 모든 도시 쌍 (A,B)에 대해서 도시 A에서 B로 가는데 필요한 비용의 최솟값을 구하는 프로그램
# 플로이드 워셜 알고리즘
# 모든 지점에서 다른 모든 지점까지의 최단 경로 계산하기

# 1) 우선 2차원 리스트를 생성해서 모두 무한으로 가게끔 만들어줌
# 2) 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화 시켜줌
# 3) a,b로 가는 비용을 c라 설정하고 넣어줌
# 4) 플로이드 워셜 알고리즘 수행 graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

INF=int(1e9)
n=int(input())
m=int(input())

graph=[[INF]*(n+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            graph[i][j]=0

for _ in range(m):
    a,b,c=map(int,input().split())
    if c<graph[a][b]:
        graph[a][b]=c

for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])

for i in range(1,n+1):
    for j in range(1,n+1):
        if graph[i][j]==INF:
            print(0,end=' ')
        else:
            print(graph[i][j],end=' ')
    print()

