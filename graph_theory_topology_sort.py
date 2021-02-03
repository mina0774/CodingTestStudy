# 위상 정렬

# 방향 그래프의 모든 노드를 방향성에 거스르지 않도록 순서대로 나열하는 것

from collections import deque

# 노드 개수, 간선 개수 입력받기
v,e=map(int,input().split())
# 모든 노드의 진입차수는 0으로 초기화
indegree=[0]*(v+1)
# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph=[[] for i in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력 받기
for _ in range(e):
    a,b=map(int,input().split())
    # 정점 A에서 B로 이동 가능
    graph[a].append(b)
    indegree[b]+=1

# 위상 정렬 함수
def topology_sort():
    # 알고리즘 수행 결과를 담을 리스트
    result=[]
    # 큐 기능을 위한 deque 라이브러리 활용
    q=deque()

    # 처음 시작 할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)

    # 큐가 비어있을 때까지 반복
    while q:
        # 큐에서 원소 꺼내기
        now=q.popleft()
        result.append(now)

        # 해당 원소에 연결된 노드들의 진입차수에서 1빼기
        for i in graph[now]:
            indegree[i]-=1
            # 새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i]==0:
                q.append(i)

    # 위상정렬 수행한 결과 출력
    for i in result:
        print(i,end=' ')

topology_sort()
