# dfs와 bfs
# n-정점의 개수, m-간선의 개수, v-시작점
from collections import deque
n,m,v=map(int,input().split())

graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for a in graph:
    a.sort()

# dfs 스택 이용
def dfs(graph,v,visited):

    visited[v]=1
    print(v,end=' ')

    for now in graph[v]:
        if visited[now]==0: # 방문하지 않은 노드면
            visited[now]=1
            dfs(graph,now,visited)

# bfs 큐 이용
def bfs(graph,v,visited):
    q=deque([v])
    visited[v]=1

    while q:
        nows=q.popleft()
        print(nows,end=' ')
        for now in graph[nows]:
            if visited[now]==0: # 방문하지 않은 노드면
                # 방문처리
                visited[now]=1
                q.append(now)

visited=[0]*(n+1)
dfs(graph,v,visited)
print()
visited=[0]*(n+1)
bfs(graph,v,visited)


