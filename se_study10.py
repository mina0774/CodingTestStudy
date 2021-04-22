# 마법사 상어와 토네이도

'''
<문제<
마법사 상어가 토네이도를 배웠고, 오늘은 토네이도를 크기가 N×N인 격자로 나누어진 모래밭에서 연습하려고 한다.
위치 (r, c)는 격자의 r행 c열을 의미하고, A[r][c]는 (r, c)에 있는 모래의 양을 의미한다.
토네이도를 시전하면 격자의 가운데 칸부터 토네이도의 이동이 시작된다. 토네이도는 한 번에 한 칸 이동한다. 다음은 N = 7인 경우 토네이도의 이동이다.
토네이도가 한 칸 이동할 때마다 모래는 다음과 같이 일정한 비율로 흩날리게 된다.
토네이도가 x에서 y로 이동하면, y의 모든 모래가 비율과 α가 적혀있는 칸으로 이동한다.
비율이 적혀있는 칸으로 이동하는 모래의 양은 y에 있는 모래의 해당 비율만큼이고, 계산에서 소수점 아래는 버린다.
α로 이동하는 모래의 양은 비율이 적혀있는 칸으로 이동하지 않은 남은 모래의 양과 같다.
모래가 이미 있는 칸으로 모래가 이동하면, 모래의 양은 더해진다.
위의 그림은 토네이도가 왼쪽으로 이동할 때이고, 다른 방향으로 이동하는 경우는 위의 그림을 해당 방향으로 회전하면 된다.
토네이도는 (1, 1)까지 이동한 뒤 소멸한다. 모래가 격자의 밖으로 이동할 수도 있다. 토네이도가 소멸되었을 때, 격자의 밖으로 나간 모래의 양을 구해보자.

<입력>
첫째 줄에 격자의 크기 N이 주어진다. 둘째 줄부터 N개의 줄에는 격자의 각 칸에 있는 모래가 주어진다. r번째 줄에서 c번째 주어지는 정수는 A[r][c] 이다.

<출력>
격자의 밖으로 나간 모래의 양을 출력한다.
'''
n=int(input())
board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))

# 격자 바깥으로 나간 모래의 양
ans=0

# 바람의 방향에 따른 모래 비율
rate_left = [[0,0,2,0,0],[0,10,7,1,0],[5,'a',0,0,0],[0,10,7,1,0],[0,0,2,0,0]]
rate_down = [[0,0,0,0,0],[0,1,0,1,0],[2,7,0,7,2],[0,10,'a',10,0],[0,0,5,0,0]]
rate_right = [[0,0,2,0,0],[0,1,7,10,0],[0,0,0,'a',5],[0,1,7,10,0],[0,0,2,0,0]]
rate_up = [[0,0,5,0,0],[0,10,'a',10,0],[2,7,0,7,2],[0,1,0,1,0],[0,0,0,0,0]]

def spread(board,rate,nx,ny):
    global ans
    # y의 좌표를 rate 배열의 좌표에 대응되게 할 수 있도록 설정
    a,b=nx-2,ny-2

    # y에서 빠져나간 모래의 총 양
    temp=0

    for i in range(5):
        for j in range(5):
            if rate[i][j]!='a' and rate[i][j]!=0:
                if 0<=i+a<n and 0<=j+b<n:
                    board[i+a][j+b]+=board[nx][ny]*rate[i][j]//100
                else:
                    # 범위 바깥으로 나갔을 경우, 격자 바깥으로 나간 모래
                    ans+=board[nx][ny]*rate[i][j]//100
                temp += board[nx][ny]*rate[i][j]//100
            elif rate[i][j]=='a':
                a_pos=(i,j)

    # 나머지 a 처리
    if 0<=a_pos[0]+a<n and 0<=a_pos[1]+b<n:
        board[a_pos[0]+a][a_pos[1]+b]+=board[nx][ny]-temp
    else:
        ans+=board[nx][ny]-temp

    # y자리 초기화
    board[nx][ny]=0

    return board

x,y=n//2,n//2

dirs=[(0,-1),(1,0),(0,1),(-1,0)]

time=1
flag=0

while flag!=1:
    for i in range(4):
        for j in range(time):
            x+=dirs[i][0]
            y+=dirs[i][1]

            if i==0:
                board=spread(board,rate_left,x,y)
            elif i==1:
                board = spread(board, rate_down, x, y)
            elif i==2:
                board = spread(board,rate_right,x,y)
            else:
                board = spread(board, rate_up, x, y)

            if (x,y)==(0,0):
                flag=1
                break

        if i==1 or i==3:
            time+=1

        if flag==1:
            print(ans)
            break


