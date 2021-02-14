# 볼링공 고르기 - sw 마에스트로 입학 테스트
# 그리디 문제
# N 볼링공 개수, M 공의 최대 무게
n,m=map(int,input().split())
data=list(map(int,input().split()))

# 1~10까지의 무게를 담을 수 있는 리스트
array=[0]*11

# 각 무게에 해당하는 개수 저장
for x in data:
    array[x]+=1

result=0

for i in range(1,n+1):
    n=n-array[i]
    result+=array[i]*n

print(result)