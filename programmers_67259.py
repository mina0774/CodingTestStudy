# n*n 격자
# 출발점 (0,0) / 도착점 (n-1,n-1)
# 자동차가 무사히 도착점에 도달할 수 있도록 경주로 건설
# 상하, 좌우 연결 (직선도로) : 100원, 직선도로가 직각으로 만나는 지점(코너) : 500원
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
from collections import deque

def solution(board):
    answer = 9999999
    q = deque()
    # 위치 x,y ,바라보는 방향, 비용
    q.append((0, 0, -1, 0))
    visited = {(0, 0, 0): 0, (0, 0, 1): 0, (0, 0, 2): 0, (0, 0, 3): 0}

    n = len(board)

    while q:
        x, y, dir, cost = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] == 0:
                ncost = cost
                if dir == -1:
                    ncost += 100
                # 진행 방향이 평행한 경우
                elif (dir - d) % 2 == 0:
                    ncost += 100
                # 진행 방향이 수직인 경우
                elif (dir - d) % 2 == 1:
                    ncost += 600

                if nx == n - 1 and ny == n - 1:
                    answer = min(answer, ncost)
                elif visited.get((nx, ny, d)) is None or visited.get((nx, ny, d)) > ncost:
                    q.append((nx, ny, d, ncost))
                    visited[(nx, ny, d)] = ncost
    return answer