# 일반적인 풀이 방
n,m,k = map(int,input().split())
data=list(map(int,input().split()))

data.sort()
first=data[n-1]
second=data[n-2]

result=0

while True:
    for i in range(k):
        if m==0:
            break
        result+=first
        m-=1
    if m==0:
        break
    result+=second
    m-=1

print(result)

# m의 크기가 100억 이상이 된다면? 위와 같은 방식은 시간 초과 발생
# 연산을 줄일 수 있는 방법 -> 반복되는 수열에 대해 파악해야함
n,m,k = map(int,input().split())
data=list(map(int,input().split()))

data.sort()
first=data[n-1]
second=data[n-2]

result=0

# 가장 큰 수가 더해지는 횟수 계산
count=int(m/(k+1))*k+m%(k+1)

result+=(count)*first
result+=(m-count)*second

print(result)


