# 위상정렬 알고리즘

from collections import deque

# 노드 개수와 간선의 개수 입력 받기
v,e=map(int,input().split())
indegree=[0]*(v+1)

graph=[[] for i in range(v+1)]

# 방향 그래프의 모든 간선 정보를 입력받기
for _ in range(e):
    a,b=map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

# 위상 정렬 함수
def topology_sort():
    # 알고리즘 수행 결과를 담을 리스트
    result=[]
    # 큐 기능을 위한 deque 라이브러리 사용
    q=deque()

    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)

    # 큐가 빌때까지 반복
    while q:
        now=q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i]-=1

            if indegree[i]==0:
                q.append(i)

    for i in result:
        print(i,end=' ')

topology_sort()
