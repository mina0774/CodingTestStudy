# 음료수 얼려먹기
# n,m을 공백을 구분하여 입력 받기
n,m=map(int,input().split())

# 맵 정보 입력 받기
graph=[]
for i in range(n):
    graph.append(list(map(int,input())))

# dfs로 특정 노드를 방문한 뒤에 연결된 모든 노드를 빙문
def dfs(x,y):

    if x<=-1 or x>=n or y<=-1 or y>=n:
        return False

    if graph[x][y]==0:
        graph[x][y]=1
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True

    return False

result=0
for i in range(n):
    for j in range(m):
        if dfs(i,j)==True:
            result+=1

print(result)