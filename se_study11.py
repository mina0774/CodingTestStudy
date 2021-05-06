# 낚시왕
'''
<문제>
낚시왕이 상어 낚시를 하는 곳은 크기가 R×C인 격자판으로 나타낼 수 있다.
격자판의 각 칸은 (r, c)로 나타낼 수 있다.
r은 행, c는 열이고, (R, C)는 아래 그림에서 가장 오른쪽 아래에 있는 칸이다.
칸에는 상어가 최대 한 마리 들어있을 수 있다. 상어는 크기와 속도를 가지고 있다.

낚시왕은 처음에 1번 열의 한 칸 왼쪽에 있다. 다음은 1초 동안 일어나는 일이며, 아래 적힌 순서대로 일어난다.
낚시왕은 가장 오른쪽 열의 오른쪽 칸에 이동하면 이동을 멈춘다.

낚시왕이 오른쪽으로 한 칸 이동한다.
낚시왕이 있는 열에 있는 상어 중에서 땅과 제일 가까운 상어를 잡는다. 상어를 잡으면 격자판에서 잡은 상어가 사라진다.
상어가 이동한다.
상어는 입력으로 주어진 속도로 이동하고, 속도의 단위는 칸/초이다.
상어가 이동하려고 하는 칸이 격자판의 경계를 넘는 경우에는 방향을 반대로 바꿔서 속력을 유지한채로 이동한다.

왼쪽 그림의 상태에서 1초가 지나면 오른쪽 상태가 된다.
상어가 보고 있는 방향이 속도의 방향, 왼쪽 아래에 적힌 정수는 속력이다. 왼쪽 위에 상어를 구분하기 위해 문자를 적었다.
상어가 이동을 마친 후에 한 칸에 상어가 두 마리 이상 있을 수 있다. 이때는 크기가 가장 큰 상어가 나머지 상어를 모두 잡아먹는다.
낚시왕이 상어 낚시를 하는 격자판의 상태가 주어졌을 때, 낚시왕이 잡은 상어 크기의 합을 구해보자.

<입력>
첫째 줄에 격자판의 크기 R, C와 상어의 수 M이 주어진다. (2 ≤ R, C ≤ 100, 0 ≤ M ≤ R×C)
둘째 줄부터 M개의 줄에 상어의 정보가 주어진다. 상어의 정보는 다섯 정수 r, c, s, d, z (1 ≤ r ≤ R, 1 ≤ c ≤ C, 0 ≤ s ≤ 1000, 1 ≤ d ≤ 4, 1 ≤ z ≤ 10000) 로 이루어져 있다.
(r, c)는 상어의 위치, s는 속력, d는 이동 방향, z는 크기이다. d가 1인 경우는 위, 2인 경우는 아래, 3인 경우는 오른쪽, 4인 경우는 왼쪽을 의미한다.
두 상어가 같은 크기를 갖는 경우는 없고, 하나의 칸에 둘 이상의 상어가 있는 경우는 없다.

<출력>
낚시왕이 잡은 상어 크기의 합을 출력한다.
'''
def sharkMove():
    temp=[[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if a[i][j]!=0:
                x,y,s,d,z=i,j,a[i][j][0],a[i][j][1],a[i][j][2]
                while s>0:
                    x+=dx[d]
                    y+=dy[d]
                    if 0<=x<R and 0<=y<C:
                        s-=1
                    else:
                        x-=dx[d]
                        y-=dy[d]
                        if d==0: d=1
                        elif d==1: d=0
                        elif d==2: d=3
                        else: d=2
                if temp[x][y]==0 or temp[x][y][2]<z:
                    temp[x][y]=[a[i][j][0],d,z]
    return temp
dx=[-1,1,0,0]
dy=[0,0,1,-1]

R,C,M=map(int,input().split())
a=[[0]*C for _ in range(R)]
for _ in range(M):
    # s 속력, d 이동방향, z 크기
    r,c,s,d,z=map(int,input().split())
    a[r-1][c-1]=[s,d-1,z]

result=0
for j in range(C):
    for i in range(R):
        if a[i][j] !=0:
            result+=a[i][j][2]
            a[i][j]=0
            break
    a=sharkMove()
print(result)