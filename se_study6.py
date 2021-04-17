# 모노미노도미노2 (시뮬레이션)

'''
<입력>
첫째 줄에 블록을 놓은 횟수 N(1 ≤ N ≤ 10,000)이 주어진다.
둘째 줄부터 N개의 줄에 블록을 놓은 정보가 한 줄에 하나씩 순서대로 주어지며, t x y와 같은 형태이다.
t = 1: 크기가 1×1인 블록을 (x, y)에 놓은 경우
t = 2: 크기가 1×2인 블록을 (x, y), (x, y+1)에 놓은 경우
t = 3: 크기가 2×1인 블록을 (x, y), (x+1, y)에 놓은 경우
블록이 차지하는 칸이 빨간색 칸의 경계를 넘어가는 경우는 입력으로 주어지지 않는다.

<출력>
첫째 줄에 블록을 모두 놓았을 때 얻은 점수를 출력한다.
둘째 줄에는 파란색 보드와 초록색 보드에서 타일이 들어있는 칸의 개수를 출력한다.
'''

n=int(input())

green=[[0 for _ in range(4)] for _ in range(6)]
blue=[[0 for _ in range(6)] for _ in range(4)]

answer=0

# 열 정보 고정
def drop_green(t,y):
    x=0 # 행 정보
    if t==1:
        for i in range(6):
            if green[i][y]==1:
                break
            x+=1
        # 실제 행의 위치
        x-=1
        green[x][y]=1
    elif t==2:
        for i in range(6):
            if green[i][y]==1 or green[i][y+1]==1:
                break
            x+=1
        # 실제 행의 위치
        x-=1
        green[x][y]=1
        green[x][y+1]=1
    elif t==3:
        for i in range(6):
            if green[i][y]==1:
                break
            x+=1
        # 실제 행의 위치
        x-=1
        green[x][y]=1
        green[x-1][y]=1


# 행 정보 고정
def drop_blue(t,x):
    y=0
    if t==1:
        for i in range(6):
            if blue[x][i]==1:
                break
            y+=1
        # 실제 열의 위치
        y-=1
        blue[x][y]=1
    elif t==2:
        for i in range(6):
            if blue[x][i]==1:
                break
            y+=1
        # 실제 열의 위치
        y-=1
        blue[x][y]=1
        blue[x][y-1]=1
    elif t==3:
        for i in range(6):
            if blue[x][i]==1 or blue[x+1][i]==1:
                break
            y+=1
        # 실제 열의 위치
        y-=1
        blue[x][y]=1
        blue[x+1][y]=1

# 행 or 열 삭제 기능
def remove(color,index):
    if color=='green':
        for i in range(index,-1,-1):
            # 0번째 행 삭제
            if i==0:
                for j in range(4):
                    green[i][j]=0
                return
            for j in range(4):
                green[i][j]=green[i-1][j]
    elif color =='blue':
        for j in range(index,-1,-1):
            # 0번째 열 삭제
            if j==0:
                for i in range(4):
                    blue[i][j]=0
                return
            for i in range(4):
                blue[i][j]=blue[i][j-1]

# 2-5번 행 or 열 가득 찼는지 확인하기
def check():
    global answer
    # green 확인
    for i in range(2,6):
        cnt=0
        for j in range(4):
            if green[i][j]==1:
                cnt+=1
        if cnt==4:
            remove('green',i)
            answer+=1

    # blue 확인
    for j in range(2,6):
        cnt=0
        for i in range(4):
            if blue[i][j]==1:
                cnt+=1
        if cnt==4:
            remove('blue',j)
            answer+=1

# 0,1 행 or 열 밝은 열 확인하기
# 해당 영역에 블록이 존재하면 제일 마지막 행 or 열 삭제
def checkLightArea():

    # green 확인
    for i in range(2):
        for j in range(4):
            if green[i][j]==1:
                remove('green',5)
                break
    # blue 확인
    for j in range(2):
        for i in range(4):
            if blue[i][j]==1:
                remove('blue',5)
                break


for _ in range(n):
    t,x,y=map(int,input().split())

    drop_blue(t,x)
    drop_green(t,y)

    check()
    checkLightArea()

block_cnt=0
for i in range(2,6):
    for j in range(4):
        if green[i][j]==1:
            block_cnt+=1
for i in range(4):
    for j in range(2,6):
        if blue[i][j]==1:
            block_cnt+=1

print(answer)
print(block_cnt)