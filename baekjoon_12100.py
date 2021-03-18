# 2048 (Easy)

'''
<문제>
2048 게임은 4×4 크기의 보드에서 혼자 즐기는 재미있는 게임이다. 이 링크를 누르면 게임을 해볼 수 있다.

이 게임에서 한 번의 이동은 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동시키는 것이다.
이때, 같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지게 된다.
한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다.
(실제 게임에서는 이동을 한 번 할 때마다 블록이 추가되지만, 이 문제에서 블록이 추가되는 경우는 없다)

<입력>
첫째 줄에 보드의 크기 N (1 ≤ N ≤ 20)이 주어진다.
둘째 줄부터 N개의 줄에는 게임판의 초기 상태가 주어진다.
0은 빈 칸을 나타내며, 이외의 값은 모두 블록을 나타낸다.
블록에 쓰여 있는 수는 2보다 크거나 같고, 1024보다 작거나 같은 2의 제곱꼴이다.
블록은 적어도 하나 주어진다.

<출력>
최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록을 출력한다.
'''


import copy

n=int(input())
board=[]
for i in range(n):
    board.append(list(map(int,input().split())))
answer=0

# 상,하,좌,우 idx로 이동하는 함수
'''
옮기는 경우의 수는 3가지로 다음과 같습니다.

앞의 숫자가 0이라면 자신의 숫자를 앞의 숫자에 옮깁니다.
앞의 숫자가 자신과 같다면 앞의숫자의 두배를 해줍니다.
앞의 숫자와 자신이 다르면 인덱스를 하나 늘리고 그자리에 넣어줍니다.
'''
def move(idx):

    if idx==0: # 상
        for j in range(n):
            idx=0
            for i in range(1,n):
                if board[i][j]:
                    temp=board[i][j]
                    board[i][j]=0
                    if board[idx][j]==0:
                        board[idx][j]=temp
                    elif board[idx][j]==temp:
                        board[idx][j]=temp*2
                        idx+=1
                    else:
                        idx+=1
                        board[idx][j]=temp
    elif idx==1: # 하
        for j in range(n):
            idx=n-1
            for i in range(n-2,-1,-1):
                if board[i][j]:
                    temp=board[i][j]
                    board[i][j]=0
                    if board[idx][j]==0:
                        board[idx][j]=temp
                    elif board[idx][j]==temp:
                        board[idx][j]=temp*2
                        idx-=1
                    else:
                        idx-=1
                        board[idx][j]=temp
    elif idx==2: # 좌
        for i in range(n):
            idx=0
            for j in range(1,n):
                if board[i][j]:
                    temp=board[i][j]
                    board[i][j]=0
                    if board[i][idx]==0:
                        board[i][idx]=temp
                    elif board[i][idx]==temp:
                        board[i][idx]=temp*2
                        idx+=1
                    else:
                        idx+=1
                        board[i][idx]=temp
    elif idx==3: # 우
        for i in range(n):
            idx=n-1
            for j in range(n-2,-1,-1):
                if board[i][j]:
                    temp=board[i][j]
                    board[i][j]=0
                    if board[i][idx]==0:
                        board[i][idx]=temp
                    elif board[i][idx]==temp:
                        board[i][idx]=temp*2
                        idx-=1
                    else:
                        idx-=1
                        board[i][idx]=temp


def dfs(count):
    global answer,board
    if count==5:
        for i in range(n):
            answer=max(answer,max(board[i]))
        return

    temp_board=copy.deepcopy(board)
    for i in range(4):
        move(i)
        dfs(count+1)
        board=copy.deepcopy(temp_board)

dfs(0)
print(answer)



