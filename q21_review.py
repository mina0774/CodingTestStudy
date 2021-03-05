# 인구이동수 - bfs 이용 문제

# n*n의 땅
# 국경선을 공유하는 두 나라의 인구차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 하루 동안 열어
# 연합을 이루고 있는 각 칸의 인수는 연합의 인구수 / 연합을 이루고 있는 칸의 개수
from collections import deque

n,l,r=map(int,input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx=[-1,0,1,0]
dy=[0,1,0,-1]

def bfs(i,j):
    temp=[]

    q=deque()
    q.append([i,j])
    temp.append([i,j])

    while q:
        x,y=q.popleft()

        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if nx>=0 and nx<n and ny>=0 and ny<n and visited[nx][ny]==0:
                if l<=abs(graph[nx][ny]-graph[x][y])<=r:
                    temp.append([nx,ny])
                    q.append([nx,ny])
                    visited[nx][ny]=1

    return temp

count=0
while True:
    visited=[[0]*n for _ in range(n)]
    isTrue=False # 인구이동 가능 여부

    for i in range(n):
        for j in range(n):
            if visited[i][j]==0:
                visited[i][j]=1
                united=bfs(i,j)

                if len(united)>1:
                    isTrue=True

                    avg=sum(graph[x][y] for x,y in united)//len(united)
                    for x,y in united:
                        graph[x][y]=avg


    if isTrue==False:
        break
    count+=1


print(count)


