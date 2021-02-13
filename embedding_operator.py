# 백준 14888번 연산자 끼워넣기

# dfs 이용

n=int(input())
data=list(map(int,input().split()))
add,sub,mul,div=map(int,input().split())

# 최솟값, 최댓값 초기화
min_value=1e9
max_value=-1e9

# 깊이 우선 탐색
def dfs(i,now):
    global min_value,max_value,add,sub,mul,div

    if i==n:
        min_value=min(min_value,now)
        max_value=max(max_value,now)
    else:
        if add>0:
            add-=1
            dfs(i+1,now+data[i])
            add+=1
        if sub>0:
            sub-=1
            dfs(i+1,now-data[i])
            sub+=1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i]))
            div += 1

dfs(1,data[0])

print(min_value)
print(max_value)

