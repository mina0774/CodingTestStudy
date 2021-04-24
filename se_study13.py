T = int(input())
# 오른쪽 0, 아래쪽 1, 왼쪽 2, 위쪽 3
dirs=[(0,1),(1,0),(0,-1),(-1,0)]
# 블록 번호의 방향에 따른 방향 변경
change=[
    (2,0,3,1),
    (2,3,1,0),
    (1,3,0,2),
    (3,2,0,1),
    (2,3,0,1)
]


def shoot(x, y, dir):
    start_x = x
    start_y = y
    score=0

    while True:
        x=x+dirs[dir][0]
        y=y+dirs[dir][1]

        if 0<=x<N and 0<=y<N:
            # 게임 끝 (블랙홀 or 시작점)
            if board[x][y]==-1 or (x,y)==(start_x,start_y):
                break
            # 블록에 부딪혔을 때
            elif 1<=board[x][y]<=5:
                score+=1
                dir=change[board[x][y]-1][dir]
            # 웜홀에 부딪혔을 때
            elif 6<=board[x][y]<=10:
                x,y=gate[(x,y)]
        # 벽에 부딪혔을 때
        else:
            score+=1
            dir=(dir+2)%4
    return score



for test_case in range(1, T + 1):

    N = int(input())
    board = []
    gate={}
    board_tmp={}
    for _ in range(N):
        board.append(list(map(int, input().split())))
    ans = 0
    for i in range(N):
        for j in range(N):
            if 6<=board[i][j]<=10:
                if board[i][j] in board_tmp:
                    gate[board_tmp[board[i][j]]]=(i,j)
                    gate[(i,j)]=board_tmp[board[i][j]]
                else:
                    board_tmp[board[i][j]]=(i,j)

    answer=-1
    for i in range(N):
        for j in range(N):
            if board[i][j]==0:
                for dir in range(4):
                    answer=max(answer,shoot(i,j,dir))

    print("#"+str(test_case)+" "+str(answer))
