# 드래곤커브
'''
<입력>
첫째 줄에 드래곤 커브의 개수 N(1 ≤ N ≤ 20)이 주어진다.
둘째 줄부터 N개의 줄에는 드래곤 커브의 정보가 주어진다.
드래곤 커브의 정보는 네 정수 x, y, d, g로 이루어져 있다.
x와 y는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대이다. (0 ≤ x, y ≤ 100, 0 ≤ d ≤ 3, 0 ≤ g ≤ 10)

입력으로 주어지는 드래곤 커브는 격자 밖으로 벗어나지 않는다. 드래곤 커브는 서로 겹칠 수 있다.
방향은 0, 1, 2, 3 중 하나이고, 다음을 의미한다.

0: x좌표가 증가하는 방향 (→)
1: y좌표가 감소하는 방향 (↑)
2: x좌표가 감소하는 방향 (←)
3: y좌표가 증가하는 방향 (↓)

<출력>
첫째 줄에 크기가 1×1인 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 것의 개수를 출력한다.
'''

# 이동방향을 리스트에 저장 시, 리스트를 뒤에서 부터 읽어 이동방향 d=(d+1)%4로 방향 리스트를 다시 생성해
N = int(input())
board = [[0] * 101 for _ in range(101)]
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
for _ in range(N):
    x, y, d, g = map(int, input().split())

    board[y][x] = 1
    move = [d]

    for _ in range(g):
        temp = []
        for i in range(len(move)):
            temp.append((move[-i - 1] + 1) % 4)
        move.extend(temp)

    for i in move:
        x += dx[i]
        y += dy[i]
        board[y][x] = 1
ans = 0
for i in range(100):
    for j in range(100):
        if board[i][j] == 1:
            if board[i + 1][j + 1] == 1 and board[i + 1][j] == 1 and board[i][j + 1] == 1:
                ans += 1
print(ans)
