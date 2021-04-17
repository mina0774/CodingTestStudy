# 청소년 상어 (dfs)

# 4*4의 공간의 한 칸에 각 물고기는 번호와 방향을 가지고 있음

# 1
# 상어는 (0,0)에 있는 물고기를 먹고 (0,0)애 들어감

# 2
# 물고기는 번호가 작은 물고기부터 이동
# 물고기는 한 칸 이동 가능, 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 45도 반시계 회전
# - 이동할 수 있는 칸 (빈칸, 다른 물고기가 있는 칸- 이동시에는 서로의 위치를 바꾸는 방식)
# - 이동할 수 없는 칸 (상어 있는 칸, 공간의 경계 넘는 칸)

# 3
# 물고기의 이동 끝난 후, 상어 이동
# 상어는 (0,0)에서 물고기를 먹고 들어감, 방향은 (0,0)에 있던 물고기 방향과 동일
# 상어는 한번에 여러개 칸 이동 가능
# 물고기 있는 칸으로 이동했다면, 물고기를 먹고, 물고기의 방향을 가지게 됨
# 물고기가 없는 칸으로는 이동할 수 없음

# 1 -> 2 -> 3 -> 2 -> 3.. 반복
# 물고기 번호의 합이 최댓값이 되도록 출력
from copy import deepcopy
dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,-1,-1,-1,0,1,1,1]

# 배열에서 특정 번호의 물고기 위치를 찾아주는 함수
def findFish(array,index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0]==index:
                return (i,j)
    return None

# 물고기는 번호가 작은 물고기부터 이동
# 물고기는 한 칸 이동 가능, 각 물고기는 방향이 이동할 수 있는 칸을 향할 때까지 45도 반시계 회전
# - 이동할 수 있는 칸 (빈칸, 다른 물고기가 있는 칸- 이동시에는 서로의 위치를 바꾸는 방식)
# - 이동할 수 없는 칸 (상어 있는 칸, 공간의 경계 넘는 칸)
def moveFish(array,shark_x,shark_y):

    for i in range(1,17):
        position=findFish(array,i)
        if position is None:
            continue
        x,y=position[0],position[1]
        dir = array[x][y][1] # 방향
        for _ in range(8):
            nx,ny=x+dx[dir],y+dy[dir]
            if 0<=nx<4 and 0<=ny<4: # 공간 안에 있고
                if not (nx==shark_x and ny==shark_y): # 상어가 없는 자리라면 이동할 수 있어
                    # 우선 번호를 바꿔줘
                    array[nx][ny][0],array[x][y][0]=array[x][y][0],array[nx][ny][0]
                    # 그 이후에는 방향을 바꿔줘
                    array[nx][ny][1],array[x][y][1]=dir,array[nx][ny][1]
                    break
            dir=(dir+1)%8

# 상어가 먹을 수 있는 후보 구하는 함수
def eatFishListbyShark(array,x,y):
    positions=[]

    dir=array[x][y][1]

    for i in range(1,4):
        nx,ny=x+dx[dir],y+dy[dir]
        if 0<=nx<4 and 0<=ny<4 and 1<=array[nx][ny][0]<=16:
            positions.append([nx,ny])
        x,y=nx,ny
    return positions



# 배열 상태, 현재 상어의 위치 (x,y), 현재 먹은 물고기 번호의 합 total
def dfs(array,x,y,total):
    global answer
    arr=deepcopy(array)

    # 해당 위치의 물고기를 먹어줘야 함, 상어는 -1
    num=arr[x][y][0]
    arr[x][y][0]=-1

    # 물고기를 이동시켜줘야 함
    moveFish(arr,x,y)

    # 상어가 먹을 수 있는 후보를 구해줌
    result=eatFishListbyShark(arr,x,y)

    # 해당 먹이를 먹는 모든 과정을 탐색함
    answer=max(answer,total+num)

    for nx,ny in result:
        dfs(arr,nx,ny,total+num)

temp=[]

for _ in range(4):
    temp.append(list(map(int,input().split())))

array=[[0]*4 for _ in range(4)]

answer = 0
for i in range(4):
    for j in range(4):
        # 물고기 번호, 방향 저장
        array[i][j]=[temp[i][j*2],temp[i][j*2+1]-1]

# dfs 탐색
dfs(array,0,0,0)
print(answer)