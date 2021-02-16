# 자물쇠와 열쇠 - 구현

# 2차원 리스트 90도로 회전시키는 함수
def rotate_a_matrix_by_90_degree(a):
    # 행의 길이
    n=len(a)
    # 열의 길이
    m=len(a[0])

    # 결과 리스트
    result=[[0]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            result[j][n-i-1]=a[i][j]

    return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
    lock_length=len(new_lock)//3
    for i in range(lock_length,lock_length*2):
        for j in range(lock_length,lock_length*2):
            if new_lock[i][j]!=1:
                return False
    return True

def solution(key,lock):
    n=len(lock)
    m=len(key)

    # 자물쇠의 크기를 기존 크기보다 3배 늘리기
    new_lock=[[0]*(n*3) for _ in range(n*3)]
    # 새로운 자물쇠의 중앙 부분에 기존 자물쇠를 넣기
    for i in range(n):
        for j in range(n):
            new_lock[i+n][j+n]=lock[i][j]

    # 4가지 방향에 대해 모두 확인
    for rotation in range(4):
        # 열쇠 회전
        key=rotate_a_matrix_by_90_degree(key)

        for x in range(n*2):
            for y in range(n*2):
                # 자물쇠에 열쇠 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]+=key[i][j]
                if check(new_lock)==True:
                    return True
                # 자물쇠에 열쇠 빼기

                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j]-=key[i][j]
        return False

print(solution([[0,0,0],[1,0,0],[0,1,1]],[[1,1,1],[1,1,0],[1,0,1]]))