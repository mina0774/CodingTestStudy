from _collections import deque

# bfs 메서드 정의 Graph는 인접 리스트를 이용하여 표현
def bfs(graph,start,visited):
    # 큐 구현을 위하여 deque 라이브러리 이용
    queue=deque([start])
    # 현재 노드를 방문 처리
    visited[start]=True
    # 큐가 비어있을 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아서 출력
        v=queue.popleft()
        print(v,end=' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True


# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
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

visited=[False]*9
bfs(graph,1,visited)

