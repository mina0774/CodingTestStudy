# dfs/bfs 문제 - 백준 14502 (연구소)

# 0 빈칸 1 벽 2 바이러스개
# 바이러스는 상하좌우로 퍼져나갈 수 있음

# 연구소 크기 n * m
# 세울 수 있는 벽의 개수 3

n,m=map(int,input().split())
# 초기 맵 리스트
array=[]
# 벽을 설치한 뒤 맵 리스트
temp=[[0]*m for _ in range(n)]

dx=[-1,0,1,0]
dy=[0,-1,0,1]

result=0

for _ in range(n):
    array.append(list(map(int,input().split())))

# DFS를 이용하여 각 바이러스 사방으로 퍼지게 하기
def virus(x,y):
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        if nx>=0 and nx<n and ny>=0 and ny<m:
            if temp[nx][ny]==0:
                temp[nx][ny]=2
                virus(nx,ny)

# 현재 맵에서 안전 영역의 크기를 계산
def get_score():
    score=0
    for i in range(n):
        for j in range(m):
            if temp[i][j]==0:
                score+=1
    return score

# DFS를 이용해 울타리를 설치하면서, 매번 안전영역을 계산
def dfs(count):
    global result

    if count==3:
        for i in range(n):
            for j in range(m):
                temp[i][j]=array[i][j]
        # 각 바이러스 전파
        for i in range(n):
            for j in range(m):
                if temp[i][j]==2:
                    virus(i,j)
        # 안전 영역의 최댓값 계산
        result=max(result,get_score())
        return

    # 빈 공간에 울타리 설치
    for i in range(n):
        for j in range(m):
            if array[i][j]==0:
                array[i][j]=1
                count+=1
                dfs(count)
                array[i][j]=0
                count-=1

dfs(0)
print(result)


