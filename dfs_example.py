# 깊이 우선 탐색
# dfs 메소드 정의, Graph는 인접 리스트로 표현되어 있음
def dfs(graph, v, visited):
    # 현재 노드 방문 처리
    visited[v]=True
    print(v,end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if visited[i]==False:
            dfs(graph,i,visited)

# graph[1]= [2,3,8] 이니까 노드 1이 노드 2, 노드 3, 노드 8과 연결되어 있다는 것을 의미
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

# 처음에는 노드들을 모두 방문하지 않은 것으로 초기화
visited=[False]*9

dfs(graph,1,visited)

