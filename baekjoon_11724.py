# bfs/dfs 유형 - 연결요소의 개수
'''
<문제>
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.
<입력>
첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N×(N-1)/2)
둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
<출력>
첫째 줄에 연결 요소의 개수를 출력한다.
'''

import sys
# python은 재귀 제한이 있으므로 이 허용치를 넘어가면 오류 -> 이를 방지하기 위해 아래와 같은 코드를 사용
sys.setrecursionlimit(10000)
n,m=map(int,input().split())
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1)
for _ in range(m):
    u,v=map(int,input().split())
    graph[u].append(v)
    graph[v].append(u)

def dfs(v):
    visited[v]=True

    for e in graph[v]:
        if not visited[e]:
            dfs(e)
answer=0
for j in range(1,n+1):
    if not visited[j]:
        dfs(j)
        answer+=1
print(answer)