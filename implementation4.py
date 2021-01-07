# N,M을 공백으로 구분하여 입력 받기
n,m = map(int,input().split())

# 방문한 위치를 저장하기 위한 맵
visit=[[0]*m for _ in range(n)]

# 현재 캐릭터 X좌표, Y좌표, 방향 입력 받기
x,y,direction=map(int,input().split())
# 현재 좌표는 방문 처리
visit[x][y]=1

# 전체 맵에 대한 정보 입력 받기
array=[]
for i in range(n):
    array.append(list(map(int,input().split())))

# 북, 동, 남, 서 방향 정의
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 왼쪽으로 회전하는 함수
def turn_left():
    global direction
    direction-=1
    if direction==-1:
        direction=3

# 시뮬레이션 시작
count=1
turn_time=0
while True:
    turn_left()
    nx=x+dx[direction]
    ny=y+dy[direction]

    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우에는 이동
    if visit[nx][ny]!=1 and array[nx][ny]!=1:
        # 이동했으니까 방문했다고 반드시 표시해주
        visit[nx][ny]=1
        x=nx
        y=ny
        count+=1
        turn_time=0
    # 회전한 이후 정면에 가보지 않은 칸이 존재하지 않는 경우
    else:
        turn_time+=1

        if turn_time==4:
            nx=x-dx[direction]
            ny=y-dy[direction]

            if array[nx][ny]==1:
                break
            else:
                x=nx
                y=nx
            turn_time=0

print(count)