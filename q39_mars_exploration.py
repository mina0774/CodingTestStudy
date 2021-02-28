# 최단 경로 문제 - 다익스트라 문제 ( 화성 탐색 )
# 다익스트라는 우선순위 큐를 사용해야함
# 우선순위큐는 heapq를 import, heapq.heappop(q)

import heapq
import sys

input=sys.stdin.readline
INF=int(1e9)

dx=[-1,0,1,0]
dy=[0,1,0,-1]

t=int(input())
for _ in range(t):
    n=int(input())
    graph=[]
    for _ in range(n):
        graph.append(list(map(int,input().split())))

    # 최단 거리 테이블을 모두 무한으로 초기화
    distance=[[INF] * n for _ in range(n)]

    # 시작 위치는 0,0
    x,y=0,0
    q=[(graph[x][y],x,y)]
    distance[x][y]=graph[x][y]

    while q:
        # 가장 최단거리가 짧은 노드를 꺼냄
        dist,x,y=heapq.heappop(q)

        # 만약, 현재 노드가 이미 처리된 적이 있다면 무시
        if distance[x][y] < dist:
            continue

        # 현재 노드와 연결된 인접 노드를 확인
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            cost=dist+graph[nx][ny]
            if distance[nx][ny] > cost:
                distance[nx][ny]=cost
                heapq.heappush(q,(cost,nx,ny))

    print(distance[n-1][n-1])
