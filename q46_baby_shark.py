# 아기상어 - 삼성전자 공채

# n*n 크기의 공간 / m마리 물고기 / 1마리 아기 상어
# 한 칸에 물고기 최대 1마리
# 아기 상어 크기 = 2, 1초에 상하좌우로 인접한 한 칸씩 이동
# 아기 상어의 크기는 자신의 크기 만큼의 물고기수를 먹을 경우 1 증가
# 아기 상어는 자기 자신보다 큰 물고기가 있는 칸은 지나갈 수 없고 나머지 칸은 이동 가능
# 아기 상어는 자신의 크기보다 작은 물고기 먹을 수 있음
# 자신이랑 크기가 같은 물고기는 먹을 수 없지만 지나갈 수는 있음

# 더 이상 먹을 수 있는 물고기가 공간에 없으면 엄마 상어에게 도움 요청
# 먹을 수 있는 물고기 1마리라면 그 물고기 먹으러감
# 먹을 수 있는 물고기가 여러 마리면 가장 가까운 물고리를 먹으러 감 (거리는 지나가야하는 칸의 개수)
# 거리가 가까운 물고기가 많으면, 가장 위에, 가장 왼쪽에 있는 물고기를 먹음

# 0 - 빈 칸
# 9 - 아기 상어의 위치
# 1,2,3,4,5,6 - 칸에 있는 물고기 크기

# bfs 이용
from collections import deque
INF=int(1e9)
n=int(input())
graph=[]
for i in range(n):
    graph.append(list(map(int,input().split())))

# 아기 상어의 현재 크기 변수
now_size=2
# 아기 상어의 현재 위치 변수
now_x,now_y=0,0

# 아기 상어의 시작 위치를 찾고, 그 위치엔 아무것도 없다고 처리
for i in range(n):
    for j in range(n):
        if graph[i][j]==9:
            now_x,now_y=i,j
            graph[now_x][now_y]=0

dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 모든 위치까지의 최단 거리만 계산하는 함수
def bfs():
    # 값이 -1이라면 도달할 수 없다는 의미(초기화)
    dist=[[-1]*n for _ in range(n)]
    # 시작 위치는 도달이 가능하다고 보며 거리는 0
    q=deque([(now_x,now_y)])
    dist[now_x][now_y]=0

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx>=0 and nx<n and ny>=0 and ny<n:
                if graph[nx][ny]<=now_size and dist[nx][ny]==-1:
                    dist[nx][ny]=dist[x][y]+1
                    q.append((nx,ny))
    # 최단거리 테이블 반환
    return dist

# 최단거리 테이블이 주어졌을 때, 먹을 물고기를 찾는 함수
def find(dist):
    x,y=0,0
    min_dist=INF

    for i in range(n):
        for j in range(n):
            # 도달이 가능하면서 먹을 수 있는 물고기일 때
            if dist[i][j]!=-1 and 1<=graph[i][j] and graph[i][j]<now_size:
                # 가장 가까운 물고기 1마리만 선택
                if dist[i][j]<min_dist:
                    x,y=i,j
                    min_dist=dist[i][j]
    # 먹을 수 있는 물고기가 없는 경우
    if min_dist==INF:
        return None
    # 먹을 수 있는 물고기의 위치와 최단 거리
    else:
        return x,y,min_dist

result=0 # 물고기를 먹을 수 없을 때까지의 소요 시간
ate=0 # 현재 크기에서 먹을 물고기의 수

while True:

    value = find(bfs())

    if value==None:
        print(result)
        break
    else:
        now_x=value[0]
        now_y=value[1]

        result+=value[2]

        # 먹은 위치에는 이제 아무것도 없도록 처리
        graph[now_x][now_y]=0
        ate+=1

        # 자신의 현재 크기 이상으로 먹은 경우에 크기를 증가
        if ate>=now_size:
            ate=0
            now_size+=1


