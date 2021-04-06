# 백준 19947 투자의 귀재 - dp
'''
문제
2020년에 학교로 복학한 주형이는 월세를 마련하기 위해서 군 적금을 깨고 복리 투자를 하려고 한다.

주형이가 하려는 투자에는 3가지 방법의 투자 방식이 있다.

1년마다 5%의 이율을 얻는 투자 (A)
3년마다 20%의 이율을 얻는 투자 (B)
5년마다 35%의 이율을 얻는 투자 (C)
투자를 할 때에는 다음과 같은 주의점이 있다.

투자의 기한(1년, 3년, 5년)을 채우는 시점에 이율이 반영되며, 그 사이에는 돈이 늘어나지 않는다.
투자 방식은 매년 바꿀 수 있다.
매번 이율은 소수점 이하를 버림 해서 받는다.
예를 들어서, 지금 가진 돈이 11111원이면, A 방식이면 1년 후에 555원, B 방식이면 3년 후에 2,222원, C 방식이면 5년 후에 3,888원을 이자로 받을 수 있다. 만약 C 방식으로 투자했지만 4년이 지난 시점이라면 받을 수 있는 이자는 0원이다.

주형이의 초기 비용이 H원일 때, Y년이 지난 시점에 가장 많은 금액을 얻을 수 있는 투자 패턴을 분석하고 그 금액을 출력하자.

입력
첫째 줄에 초기 비용 H와 투자 기간 Y가 주어진다.

모든 입력은 정수로 주어진다.

출력
가장 많은 이득을 얻었을 때의 총 자산을 소수점을 모두 버리고 정수로 출력한다.
'''

h,y=map(int,input().split())

dp=[0]*(y+1)
dp[0]=h

for i in range(1,y+1):
    if i-1>=0 and dp[i-1]:
        dp[i]=max(dp[i],int(dp[i-1]*1.05))
    if i-3>=0 and dp[i-3]:
        dp[i]=max(dp[i],int(dp[i-3]*1.2))
    if i-5>=0 and dp[i-5]:
        dp[i]=max(dp[i],int(dp[i-5]*1.35))

print(dp[y])