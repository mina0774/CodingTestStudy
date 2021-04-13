# 탈주범 검거 - dfs
from collections import deque

T = int(input())

# 각 터널의 종류에 따라 이동가능한 방향 딕셔너리 형태로 표현
tunnel={
    0:(),
    1:((1,0),(0,1),(-1,0),(0,-1)),
    2:((1,0),(-1,0)),
    3:((0,1),(0,-1)),
    4:((-1,0),(0,1)),
    5:((1,0),(0,1)),
    6:((1,0),(0,-1)),
    7:((-1,0),(0,-1))
}


for test_case in range(1, T + 1):
    # 세로크기, 가로크기, 맨홀뚜껑 위치 세로, 가로, 탈출 후 소요된 시간
    n, m, r, c, l = map(int, input().split(" "))
    array = []
    visited=[[0]*m for _ in range(n)]

    for i in range(n):
        array.append(list(map(int, input().split())))

    q=deque()
    q.append([r,c])
    visited[r][c]=1
    cnt=1
    while q:
        x,y=q.popleft()
        for dx,dy in tunnel[array[x][y]]:
            nx=x+dx
            ny=y+dy
            if 0<=nx<n and 0<=ny<m:
                if (-dx,-dy) in tunnel[array[nx][ny]]: # 터널 연결 상태 꼭 확인하기!!!!!!
                    if visited[nx][ny]==0:
                        q.append([nx,ny])
                        visited[nx][ny]=visited[x][y]+1
                        if visited[nx][ny]<=l:
                            cnt+=1


    print("#"+str(test_case)+" "+str(cnt))
