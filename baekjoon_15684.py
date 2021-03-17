# 사다리조작
# 완전 탐색 (BruteForce)

from sys import exit

n,m,h=map(int,input().split())

if m==0:
    print(0)
    exit()

bridge=[[False]*n for _ in range(h)]

for _ in range(m):
    a,b=map(int,input().split())
    bridge[a-1][b-1]=True

# i번째 세로선의 결과가 i가 나오는지 확인하는 함수
def check():
    for start in range(n):
        k=start
        for i in range(h):
            if bridge[i][k]==True:
                k+=1
            elif k>0 and bridge[i][k-1]==True:
                k-=1
        if start!=k:
            return False
    return True

def brute_force(cnt,x,y):
    global ans
    if check():
        ans=min(ans,cnt)
        return
    # i번째에 도달하지 않고, 현재 cnt가 3이거나 ans값을 초과하면, 종료
    elif cnt==3 or ans<=cnt:
        return

    for i in range(x,h):
        if i==x:
            k=y
        else:
            k=0

        for j in range(k,n-1):
            if not bridge[i][j] and not bridge[i][j+1]:
                bridge[i][j]=True
                brute_force(cnt+1,i,j+2)
                bridge[i][j]=False

# ans의 최대값은 3이므로 4로 초기화해주고 시작
ans=4
brute_force(0,0,0)
if ans<4:
    print(ans)
else:
    print(-1)