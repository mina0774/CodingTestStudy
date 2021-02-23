# 다이나믹 프로그래밍 - 퇴사 (백준 14501)

n=int(input())
# 상담을 완료하는데 걸리는 기간
t=[]
# 상담을 완료했을 때 받을 수 있는 금액
p=[]

# 다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화
dp=[0]*(n+1)
max_value=0

for _ in range(n):
    x,y=map(int,input().split())
    t.append(x)
    p.append(y)

for i in range(n-1,-1,-1):
    time=t[i]+i
    # 상담이 기간 안에 끝나는 경우
    if time<=n:
        dp[i]=max(p[i]+dp[time],max_value)
        max_value=dp[i]
    else:
        dp[i]=max_value

print(max_value)
