# 미로 탈출
from _collections import deque
n,m=map(int,input().split())

graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

# 이동 방향 정의 좌,우,상,하
dx=[-1,1,0,0]
dy=[0,0,-1,1]

# BFS 소스코드 구현
def bfs(x,y):
    queue=deque()
    queue.append((x,y))

    while queue:
        x,y=queue.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            # 범위를 벗어날 경우 무시
            if nx<=-1 or nx>=n or ny<=-1 or ny>=m:
                continue

            # 괴물이 있다면 무시
            if graph[nx][ny]==0:
                continue

            if graph[nx][ny]==1:
                graph[nx][ny]=graph[x][y]+1
                queue.append((nx,ny))
    return graph[n-1][m-1]

print(bfs(0,0))