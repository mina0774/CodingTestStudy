# 블록 이동하기 - 프로그래머스 60063 (카카오 신입 공채 1차)
from collections import deque

# 로봇의 상태를 집합 자료형으로 관리 -> 한번 방문한 자전거의 상태는 두번 방문하지 않음!
# => 예시 {(1,1),(1,2)}

# 특정 위치에서 이동 가능한 다음 위치를 모두 반환해주는 함수
def get_next_pos(pos,board):
    # 이동 가능한 위치들
    next_pos=[]

    # 현재 위치 정보 (집합 -> 리스트) 형태로 변환
    pos=list(pos)
    pos1_x,pos1_y,pos2_x,pos2_y=pos[0][0],pos[0][1],pos[1][0],pos[1][1]

    # 1) 상, 하, 좌, 우 이동 여부 처리
    dx=[-1,1,0,0]
    dy=[0,0,-1,1]
    for i in range(4):
        pos1_nx,pos1_ny,pos2_nx,pos2_ny=pos1_x+dx[i],pos1_y+dy[i],pos2_x+dx[i],pos2_y+dy[i]
        if board[pos1_nx][pos1_ny]==0 and board[pos2_nx][pos2_ny]==0:
            next_pos.append({(pos1_nx,pos1_ny),(pos2_nx,pos2_ny)})

    # 2) 회전 여부 처리
    # 현재 로봇이 가로로 놓여있는 경우
    if pos1_x==pos2_x:
        # 위쪽 or 아래쪽으로 회전
        for i in [-1,1]:
            if board[pos1_x+i][pos1_y]==0 and board[pos2_x+i][pos2_y]==0:
                next_pos.append({(pos1_x,pos1_y),(pos1_x+i,pos1_y)})
                next_pos.append({(pos2_x,pos2_y),(pos2_x+i,pos2_y)})
    # 현재 로봇이 세로로 놓여있는 경우
    elif pos1_y==pos2_y:
        # 왼쪽 or 오른쪽으로 회전
        for i in [-1,1]:
            if board[pos1_x][pos1_y+i]==0 and board[pos2_x][pos2_y+i]==0:
                next_pos.append({(pos1_x,pos1_y),(pos1_x,pos1_y+i)})
                next_pos.append({(pos2_x,pos2_y),(pos2_x,pos2_y+i)})

    return next_pos

def solution(board):
    # 맵 외곽에 벽을 두는 형태로 맵 변형
    n=len(board)
    new_board=[[1]*(n+2) for _ in range(n+2)]
    for i in range(n):
        for j in range(n):
            new_board[i+1][j+1]=board[i][j]

    # 너비 우선 탐색 (BFS) 진행
    q=deque()
    visited=[]
    # 시작 위치 설정
    pos={(1,1),(1,2)}
    q.append((pos,0))
    # 방문 처리
    visited.append(pos)

    # 큐가 빌 때까지 반복
    while q:
        pos,cost=q.popleft()

        if (n,n) in pos:
            return cost

        for next_pos in get_next_pos(pos,new_board):
            if next_pos not in visited:
                q.append((next_pos,cost+1))
                visited.append(next_pos)

print(solution([[0,0,0,1,1],[0,0,0,1,0],[0,1,0,1,1],[1,1,0,0,1],[0,0,0,0,0]]))