# brute force 문제 사다리 조작 (백준 15684)
# 시간초과~~~~~~~~~ 나중ㅇ에 해보자아아ㅏㅏ]
res=10000
n,m,h=map(int,input().split())

graph=[[0]*n for _ in range(h)]
for _ in range(m):
    a,b=map(int,input().split())
    graph[a-1][b-1]=1

# 사다리가 모두 자기 자신으로 돌아가는지 확인하는 함수
def check():
    for i in range(n):
        start=i
        for j in range(h):
            # 사다리가 현재를 기준점으로 오른쪽에 있을 경우
            if graph[j][start]:
                start+=1
            # 사다리가 현재를 기준점으로 왼쪽에 있을 경우
            elif start-1 >=0 and graph[j][start-1]:
                start-=1
        if start!=i:
            return False
    return True

def bf(start,cnt):
    global res
    if cnt<=3:
        if check():
            res=min(res,cnt)
            return

    for i in range(start,h):
        for j in range(n-1):
            # 전후로 놓인 사다리가 없고, 현재 위치도 사다리가 놓여있지 않다면
            if not graph[i][j]+graph[i][j-1]+graph[i][j+1]:
                graph[i][j]=1
                bf(i,cnt+1)
                graph[i][j]=0

bf(0,0)
if res!=10000:
    print(res)
else:
    print(-1)






