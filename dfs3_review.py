# 음료수 얼려먹기
# dfs 이용하기
# 스택의 최상단노드에 삽입, 방문처리
# 스택 인접노드 방문하지 않았을 경우 스택에 삽입 / 방문하지 않은 노드가 없을 경우 스택에서 뺌 ( 스택에 아무것도 없을 때까지 반복 )

n,m=map(int,input().split())

graph=[]
for _ in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):

    if x>=n or x<0 or y>=m or y<0:
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


