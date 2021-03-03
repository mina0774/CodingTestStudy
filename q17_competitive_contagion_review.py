# DFS/BFS 경쟁적 전염 (백준 18405) review
# BFS 이용해보자 - BFS는 큐!

# n*n 크기의 시험관
# 바이러스의 종류 1~K번까지 K가지가 있음
# 모든 바이러스는 1초마다 상,하,좌,우 방향으로 증식
# 매초 번호가 낮은 종류의 바이러스부터 증식
# 특정 칸에 이미 어떠한 바이러스가 있다면 그곳에는 바이러스 증식 불가

from collections import deque

# s초가 지난 후, x,y에 존재하는 바이러스의 종류를 출력하는 프로그램
# s초 지난 후, 해당 위치에 바이러스 존재하지 않는다면 0 출력

n,k=map(int,input().split())

# 전체 보드 정보를 담는 리스트
graph=[]
# 바이러스 정보를 담는 리스트
data=[]
for i in range(n):
    graph.append(list(map(int,input().split())))
    # 해당 위치에 바이러스 존재하는 경우, 바이러스 정보 저장
    for j in range(n):
        if graph[i][j]!=0:
            # 바이러스 종류, 시간, 위치X, 위치Y 삽입
            data.append((graph[i][j],0,i,j))

# 낮은 번호의 바이러스가 먼저 증식하므로 바이러스 종류 수능로 정렬한 후 큐에 옮기기
data.sort()
q=deque(data)

target_s,target_x,target_y=map(int,input().split())

# 바이러스가 퍼져나갈 수 있는 4가지 위치
dx=[-1,0,1,0]
dy=[0,1,0,-1]

while q:
    virus,s,x,y=q.popleft()

    # 정확히 s초가 지나거나 큐가 빌때까지 반복
    if s==target_s:
        break

    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        # 해당 위치로 이동할 수 있는 경우에
        if nx>=0 and nx<n and ny>=0 and ny<n:
            # 바이러스가 증식되지 않은 경우라면
            if graph[nx][ny]==0:
                graph[nx][ny]=virus
                q.append((virus,s+1,nx,ny))

print(graph[target_x-1][target_y-1])

