# 1로 만들기
# X가 5로 나누어떨어지면, 5로 나눔
# X가 3으로 나누어떨어지면, 3으로 나눔
# X가 2로 나누어떨어지면, 2로 나눔
# X에서 1을 뺌

# 점화식을 떠올려보자!
# Ai=min(Ai-1,Ai//2,Ai//3,Ai//5)+1
# 요 자식을 이용해서 차근차근! 밑에서부터 위로 올라가면 됨

import sys

def bottomup():
    d=[0]*30001
    n=int(input())

    for i in range(2,n+1):

        # 현재의 수에서 1을 뺀 경우
        d[i]=d[i-1]+1

        if i%2==0:
            d[i]=min(d[i],d[i//2]+1)
        if i%3==0:
            d[i]=min(d[i],d[i//3]+1)
        if i%5==0:
            d[i]=min(d[i],d[i//5]+1)

    print(d[n])

# 재귀함수 depth때문에 메모리 초과가 남
# 어떻게 해결해야할지는 아직 잘 모르겠음..
# 일단 탑다운은 이런식으로 구현할 수 있을 듯..
def topdown():
    d=[0]*30001
    n=int(input())

    def make1(x):
        if x==1:
            return 0

        if d[x]!=0:
            return d[x]

        d[x]=make1(x-1)+1

        if x%2==0:
            d[x]=min(d[x],make1(x//2)+1)
        if x%3==0:
            d[x]=min(d[x],make1(x//3)+1)
        if x%5==0:
            d[x]=min(d[x],make1(x//5)+1)

        return d[x]

    print(make1(n))

bottomup()
topdown()