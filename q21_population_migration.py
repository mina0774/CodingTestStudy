# bfs 이용하기 -> 인구이동 백준 16234

from collections import deque

# 입력 받기
n,l,r=map(int,input().split())

# 전체 나라의 정보 입력 받기
graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

# 이동 방향 지정
dx=[-1,0,1,0]
dy=[0,-1,0,1]

def bfs(i,j):
    q=deque()
    q.append([i,j])
    # 하나의 연합을 저장할 배열
    temp=[]
    temp.append([i,j])

    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if 0<=nx<n and 0<=ny<n and visit[nx][ny]==0:
                if l<=abs(graph[x][y]-graph[nx][ny])<=r:
                    temp.append([nx,ny])
                    q.append([nx,ny])
                    visit[nx][ny]=1

    # 하나의 연합을 return
    return temp

# 이동할 인구가 없을 때까지 반복
# 인구 이동 횟수
count=0
while True:
    visit=[[0]*n for _ in range(n)]
    # 인구 이동 여부
    isTrue=False
    for i in range(n):
        for j in range(n):
            if visit[i][j]==0:
                visit[i][j]=1
                united=bfs(i,j)
                if len(united)>1:
                    isTrue=True
                    num=sum(graph[x][y] for x,y in united)//len(united)
                    for x,y in united:
                        graph[x][y]=num
    # 전체를 다 돌았는데 더 이상 인구 이동이 불가하다면 while문 빠져나옴
    if not isTrue:
        break
    count+=1

print(count)
