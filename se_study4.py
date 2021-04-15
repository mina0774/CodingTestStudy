# 마법사 상어와 파이어볼
'''
<문제>
마법사 상어가 크기가 N×N인 격자에 파이어볼 M개를 발사했다.
가장 처음에 파이어볼은 각자 위치에서 이동을 대기하고 있다.
i번 파이어볼의 위치는 (ri, ci), 질량은 mi이고, 방향은 di, 속력은 si이다. 위치 (r, c)는 r행 c열을 의미한다.
격자의 행과 열은 1번부터 N번까지 번호가 매겨져 있고, 1번 행은 N번과 연결되어 있고, 1번 열은 N번 열과 연결되어 있다.
파이어볼의 방향은 어떤 칸과 인접한 8개의 칸의 방향을 의미하며, 정수로는 다음과 같다.
7	0	1
6	 	2
5	4	3
마법사 상어가 모든 파이어볼에게 이동을 명령하면 다음이 일들이 일어난다.

모든 파이어볼이 자신의 방향 di로 속력 si칸 만큼 이동한다.
이동하는 중에는 같은 칸에 여러 개의 파이어볼이 있을 수도 있다.
이동이 모두 끝난 뒤, 2개 이상의 파이어볼이 있는 칸에서는 다음과 같은 일이 일어난다.
1.같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다.
2.파이어볼은 4개의 파이어볼로 나누어진다.
3.나누어진 파이어볼의 질량, 속력, 방향은 다음과 같다.
질량은 ⌊(합쳐진 파이어볼 질량의 합)/5⌋이다.
속력은 ⌊(합쳐진 파이어볼 속력의 합)/(합쳐진 파이어볼의 개수)⌋이다.
합쳐지는 파이어볼의 방향이 모두 홀수이거나 모두 짝수이면, 방향은 0, 2, 4, 6이 되고, 그렇지 않으면 1, 3, 5, 7이 된다.
4.질량이 0인 파이어볼은 소멸되어 없어진다.
마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 구해보자.

<입력>
첫째 줄에 N, M, K가 주어진다.
둘째 줄부터 M개의 줄에 파이어볼의 정보가 한 줄에 하나씩 주어진다.
파이어볼의 정보는 다섯 정수 ri, ci, mi, si, di로 이루어져 있다.
서로 다른 두 파이어볼의 위치가 같은 경우는 입력으로 주어지지 않는다.

<출력>
마법사 상어가 이동을 K번 명령한 후, 남아있는 파이어볼 질량의 합을 출력한다.
'''
from copy import deepcopy

dx=[-1,-1,0,1,1,1,0,-1]
dy=[0,1,1,1,0,-1,-1,-1]
n,m,k=map(int,input().split())

board=[ [[] for _ in range(n) ] for _ in range(n)]

for _ in range(m):
    r,c,w,s,d=map(int,input().split())
    if w!=0:
        board[r-1][c-1].append((w,s,d))

for _ in range(k):
    n_board=[ [[] for _ in range(n) ] for _ in range(n)]

    # 파이어볼 이동
    for x in range(n):
        for y in range(n):
            if len(board[x][y])!=0:
                for i in range(len(board[x][y])):
                    nm,ns,nd=board[x][y][i]
                    nx,ny=x+dx[nd]*ns,y+dy[nd]*ns
                    nx=(nx+n)%n
                    ny=(ny+n)%n
                    n_board[nx][ny].append((nm,ns,nd))

    # 2개 이상의 파이어볼이 있는 칸을 찾아 4개의 파이어볼을 만듦
    for x in range(n):
        for y in range(n):
            if len(n_board[x][y])>1:
                cm,cs,cd=0,0,[]
                cnt = len(n_board[x][y])
                for i in range(cnt):
                    cm+=n_board[x][y][i][0]
                    cs+=n_board[x][y][i][1]
                    cd.append(n_board[x][y][i][2]%2)
                cm=int(cm/5)
                cs=int(cs/cnt)
                n_board[x][y]=[]

                if cm!=0:
                    # 합쳐진 파이어볼 방향이 모두 홀수이거나 짝수일 경우
                    if sum(cd)==0 or sum(cd)==cnt:
                        for i in range(4):
                            n_board[x][y].append((cm,cs,2*i))
                    else:
                        for i in range(4):
                            n_board[x][y].append((cm,cs,2*i+1))

    board=deepcopy(n_board)

sum=0
for x in range(n):
    for y in range(n):
        if len(board[x][y])!=0:
            for i in range(len(board[x][y])):
                sum+=board[x][y][i][0]
print(sum)


