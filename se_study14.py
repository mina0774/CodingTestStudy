# 스타트택시 (bfs/dfs)

'''
<입력>
첫 줄에 N, M, 그리고 초기 연료의 양이 주어진다. (2 ≤ N ≤ 20, 1 ≤ M ≤ N2, 1 ≤ 초기 연료 ≤ 500,000)
연료는 무한히 많이 담을 수 있기 때문에, 초기 연료의 양을 넘어서 충전될 수도 있다.
다음 줄부터 N개의 줄에 걸쳐 백준이 활동할 영역의 지도가 주어진다. 0은 빈칸, 1은 벽을 나타낸다.
다음 줄에는 백준이 운전을 시작하는 칸의 행 번호와 열 번호가 주어진다. 행과 열 번호는 1 이상 N 이하의 자연수이고, 운전을 시작하는 칸은 빈칸이다.
그다음 줄부터 M개의 줄에 걸쳐 각 승객의 출발지의 행과 열 번호, 그리고 목적지의 행과 열 번호가 주어진다.
모든 출발지와 목적지는 빈칸이고, 모든 출발지는 서로 다르며, 각 손님의 출발지와 목적지는 다르다.

<출력>
모든 손님을 이동시키고 연료를 충전했을 때 남은 연료의 양을 출력한다.
단, 이동 도중에 연료가 바닥나서 다음 출발지나 목적지로 이동할 수 없으면 -1을 출력한다.
모든 손님을 이동시킬 수 없는 경우에도 -1을 출력한다.
'''
from collections import deque
INF=int(1e9)
def findPassenger(taxi):
    q=deque()
    q.append(taxi)
    visited=[[0] * n for _ in range(n)]
    minDist=INF

    candidate=[]

    while q:
        x,y=q.popleft()
        if visited[x][y]>minDist:
            break
        if [x,y] in start:
            minDist=visited[x][y]
            candidate.append([x,y])
        else:
            for i in range(4):
                nx=x+dirs[i][0]
                ny=y+dirs[i][1]
                if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and board[nx][ny]!=1:
                    visited[nx][ny]=visited[x][y]+1
                    q.append([nx,ny])
    if candidate:
        candidate.sort()
        # 행,열,최단거리
        return candidate[0][0],candidate[0][1],visited[candidate[0][0]][candidate[0][1]]
    else:
        return -1,-1,-1

def goDest(start,end):
    q=deque()
    q.append(start)
    visited=[[0]*n for _ in range(n)]
    while q:
        x,y=q.popleft()
        if [x,y]==end:
            break
        else:
            for i in range(4):
                nx=x+dirs[i][0]
                ny=y+dirs[i][1]
                if 0<=nx<n and 0<=ny<n and visited[nx][ny]==0 and board[nx][ny]!=1:
                    visited[nx][ny]=visited[x][y]+1
                    q.append([nx,ny])
    return x,y,visited[x][y]


# n*n의 격자, m 승객수, fuel 초기 연료양
n,m,fuel=map(int,input().split())
board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))
x,y=map(int,input().split())
taxi=[x-1,y-1]

start=[]
dst=[]
for _ in range(m):
    px,py,ox,oy=map(int,input().split())
    start.append([px-1,py-1])
    dst.append([ox-1,oy-1])
dirs=[(1,0),(0,1),(-1,0),(0,-1)]

for _ in range(m):
    # 최단 경로의 손님 찾기 (행,열,최단거리)
    x,y,dist=findPassenger(taxi)

    # 손님에게 이동불가 이거나 연료가 떨어질 경우
    if dist==-1 or fuel-dist<0:
        fuel=-1
        break
    fuel-=dist

    idx=start.index([x,y])

    # 손님을 태웠으므로 손님 목록에서 제거하기 위해 변경
    start[idx]=[-1,-1]

    x2,y2,dist2=goDest([x,y],dst[idx])

    if [x2,y2] != dst[idx] or fuel-dist2<0:
        fuel=-1
        break

    fuel+=dist2
    taxi=[x2,y2]

print(fuel)