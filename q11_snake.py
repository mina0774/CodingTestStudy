# 구현 - 뱀

# 구현은 빡세구나~~~ ㅠㅠ

# 사과를 먹으면 뱀의 길이가 길어짐
# 뱀이 이리저리 기어다니다가 벽 or 자기 자신의 몸과 부딪히면 게임이 끝남

# n*n
# 뱀의 시작위치는 0,0 / 뱀의 길이는 1 / 뱀이 바라보는 방향 - 오른쪽

# 뱀은 몸 길이를 늘려 머리를 다음 칸에 위치시킴
# 이동한 칸에 사과가 있으면, 그 칸에 있던 사과는 없어짐, 꼬리는 움직이지 않음
# 이동한 칸에 사과가 없으면, 몸길이를 줄여서, 꼬리기 위치한 칸을 비워줌

n=int(input()) # 보드의 크기
k=int(input()) # 사과의 개수

# 맵 정보
board = [[0]*(n+1) for _ in range(n+1)]

# 사과의 위치
for _ in range(k):
    a,b=map(int,input().split())
    board[a][b]=1

# 방향 회전 정보 입력 / x초 후, c방향으로 회전 / 'L'이 왼쪽 방향으로 90도 / 'D'이 오른쪽 방향으로 90도
num=int(input())
info=[]
for _ in range(num):
    x,c=input().split()
    info.append((int(x),c))

# 처음에는 오른쪽을 바라보고 있으므로 (동/남/서/북)
dx=[0,1,0,-1]
dy=[1,0,-1,0]

def turn(direction,c):
    if c=='L':
        direction=(direction-1)%4
    elif c=='D':
        direction=(direction+1)%4
    return direction

def simulate():
    x,y=1,1 # 뱀의 머리 위치
    board[x][y]=2 # 뱀이 존재하는 위치를 2로 설정
    direction=0 # 처음에는 동쪽을 보고 있음
    time=0 # 시작한 뒤 지난 '초'의 시간
    index=0 # 다음에 회전할 정보
    q=[(x,y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)

    while True:
        nx=x+dx[direction]
        ny=y+dy[direction]

        # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
        if 1<=nx and nx<=n and 1<=ny and ny<=n and board[nx][ny]!=2:
            # 이동한 칸에 사과가 있으면, 그 칸에 있던 사과는 없어짐, 꼬리는 움직이지 않음
            # 이동한 칸에 사과가 없으면, 몸길이를 줄여서, 꼬리기 위치한 칸을 비워줌

            # 사과가 없다면
            if board[nx][ny]==0:
                board[nx][ny]=2
                q.append((nx,ny))
                px,py=q.pop(0)
                board[px][py]=0
            # 사과가 있다면
            if board[nx][ny]==1:
                board[nx][ny]=2
                q.append((nx,ny))

        # 벽이나 뱀의 몸통 부분과 부딪혔다면
        else:
            time+=1
            break
        x,y=nx,ny
        time+=1

        # time이 회전할 시간인 경우
        if index<num and time==info[index][0]:
            direction=turn(direction,info[index][1])
            index+=1

    return time

print(simulate())