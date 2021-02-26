# 코딩테스트 대비 복습 bfs/dfs 리뷰

# DFS
# 1) 탐색 시작 노드를 스택에 삽입하고, 방문 처리 한다.
# 2) 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면 그 인접노드를 스택에 넣고 방문처리한다. 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 3) 2번의 과정을 더 이상 수행할 수 없을 때까지 반복복

def dfs(graph,v,visited):
    # 현재 노드 방문 처리
    visited[v]=True
    print('v',end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited=[False]*9

dfs(graph,1,visited)

# BFS
# 1) 탐색 시작 노드를 큐에 삽입하고, 방문 처리 한다.
# 2) 큐에서 노드를 꺼내 해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입하고 방문 처리를 한다.
# 3) 2번의 과정을 더 이상 수행할 수 없을 때까지 반복
from collections import deque

def bfs(graph,start,visited):
    queue=deque([start])
    visited[start]=True

    while queue:
        v=queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

graph=[
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited=[False]*9

bfs(graph,1,visited)
