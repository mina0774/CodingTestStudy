# 최단 경로 문제 - 정확한 순위

# 시험을 본 학생 n명의 성적 분실
# 성적 비교 결과 일부만 가지고 있음

# 플로이드 워셜 알고리즘 이용 - 모든 지점에서 다른 모든 지점에서의 비용을 계산
# 한 지점에서 다른 지점으로 도달 가능하고, 도달 가능한 횟수가 학생들의 수와 같다면 정확한 순위를 알수있음

n,m=map(int,input().split())

INF=int(1e9)

graph=[[INF]*(n+1) for _ in range(n+1)]
# 자기 자신으로 도달하는 비용은 0으로 초기화
for i in range(1,n+1):
    graph[i][i]=0

# a<b 관계를 a->b로 나타내기
for _ in range(m):
    a,b=map(int,input().split())
    graph[a][b]=1

# 플로이드 워셜 알고리즘 이용하여 모든 지점에서 다른 모든 지점으로의 최소비용을 계산
# 즉 모든 지점에서 다른 모든 지점으로 도달할 수 있는 모든 경우의 수를 구할 수 있음
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b]=min(graph[a][b],graph[a][k]+graph[k][b])


result=0
for a in range(1,n+1):
    count = 0
    for b in range(1,n+1):
        if graph[a][b]!=INF or graph[b][a]!=INF:
            count+=1
    if count==n:
        result+=1

print(result)




