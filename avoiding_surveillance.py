from itertools import combinations

# 복도 크기
n=int(input())
board=[] # 복도 정보
teachers=[] # 모든 선생님 위치 정보
spaces=[] # 모든 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님이 존재하는 위치 저장
        if board[i][j]=='T':
            teachers.append((i,j))
        # 장애물을 설치할 수 있는 (빈 공간) 위치 저장
        if board[i][j]=='X':
            spaces.append((i,j))

# 특정 방향에 학생이 있는지 확인하는 함수
# 학생 발견 시 True, 미발견 장애물 발견 시 False
def watch(x,y,direction):
    # 왼쪽 방향으로 감시
    if direction==0:
        while y>=0:
            if board[x][y]=='S':
                return True
            if board[x][y]=='O':
                return False
            y-=1
    # 오른쪽 방향으로 감시
    if direction==1:
        while y<n:
            if board[x][y]=='S':
                return True
            if board[x][y]=='O':
                return False
            y+=1
    # 위쪽 방향으로 감시
    if direction==2:
        while x>=0:
            if board[x][y]=='S':
                return True
            if board[x][y]=='O':
                return False
            x-=1
    # 아래쪽 방향으로 감시
    if direction==3:
        while x<n:
            if board[x][y]=='S':
                return True
            if board[x][y]=='O':
                return False
            x+=1
    return False

# 장애물 설치 후에, 학생 감지 확인 함수
def process():
    # 모든 선생님의 위치를 하나씩 확인
    for x,y in teachers:
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(x,y,i):
                return True
    return False

# 학생이 발견되지 않으면 find -> True
find=False

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces,3):
    # 장애물 설치
    for x,y in data:
        board[x][y]='O'
    # 학생이 한명도 감지되지 않은 경우
    if not process():
        # 원하는 경우
        find=True
        break

    # 장애물 다시 복구
    for x,y in data:
        board[x][y]='X'

if find:
    print('YES')
else:
    print('NO')
