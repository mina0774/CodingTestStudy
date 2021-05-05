n=int(input())

lines=[]
dp=[1]*n
for _ in range(n):
    a,b=map(int,input().split())
    lines.append((a,b))
lines.sort(key=lambda x:x[0])

for i in range(n):
    for j in range(i):
        if lines[i][1]>lines[j][1]:
            dp[i]=max(dp[i],dp[j]+1)

print(n-max(dp))