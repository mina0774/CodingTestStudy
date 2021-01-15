from collections import deque

n,k=map(int,input().split())

# 전체 보드에 대한 정보를 담는 리스트
graph=[]
# 바이러스에 대한 정보를 담는 리스트
data=[]

# 보드 정보를 한 줄 단위로 입력
for i in range(n):
    graph.append(list(map(int,input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재한다면
        # 바이러스의 종류, 시간, 위치 X, 위치 Y를 삽입
        if graph[i][j]!=0:
            data.append((graph[i][j],0,i,j))

# 그 후 바이러스에 대한 정보를 정렬을 해야지
# 왜냐하면 각 바이러스는 낮은 번호부터 증식하기 때문에 sort를 해준후 queue에 넣어서 bfs를 진행해주어야겠지요??
data.sort()
q=deque(data)

# s초 후에 x와 y 자리에 놓여있는 바이러스의 종류가 무엇일까를 맞추는 문제지요
# 그러니까 s,x,y를 입력으로 받아줘야지요~
target_s,target_x,target_y=map(int,input().split())

# 바이러스는 상,하,좌,우 4가지 방향으로 퍼질 수 있지요~
# 그러니까 움직일 수 있는 방향을 정의해주자요~
dx=[-1,0,1,0]
dy=[0,1,0,-1]

# 자 이제 그럼 bfs를 이용해서 바이러스를 퍼뜨려볼까요
# bfs에 대한 복습을 해보자면
# bfs는 탐색을 시작하는 노드를 우선 큐에 삽입을 해줘야해~
# 그 후엔 큐에서 노드를 꺼내서 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입한 담에 방문 처리를 해줘야돼
# 그리고 다시 이 과정을 반복 반복해줘 큐가 비어있을 때까지 got it?

# 그럼 우선 큐가 비어있을 때까지 이 과정을 반복해야되니까 while문을 써볼까여?
while q:
    # 자 현재 큐에 들어있는 값에서 제일 처음에 들어간 값을 빼줘야겠지요
    virus,s,x,y=q.popleft()

    # 자 이제 s초가 목표 시간이 되면 당연히 반복문을 끝내줘야겠지?
    if s==target_s:
        break

    # 그래서 이제 현재 큐에서 꺼낸 노드에서 나아갈 수 있는 주변 4가지 위치를 모두 확인해보자!
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]

        # 그럼 해당 위치로 이동할 수 있는지 먼저 확인을 해봐야겠지요
        if nx>=0 and nx<n and ny>=0 and ny<n:
            # 그리고 그 위치에서 아직 바이러스가 퍼지지 않았다면 바이러스를 퍼뜨려야겠죠
            # 바이러스를 퍼뜨리고 큐에 이걸 넣어줘요~
            if graph[nx][ny]==0:
                graph[nx][ny]=virus
                q.append((virus,s+1,nx,ny))

print(graph[target_x-1][target_y-1])