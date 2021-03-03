# 다이나믹 프로그래밍 - 편집 거리

# 두개의 문자열 A,B가 주어졌을 경우
# 문자열 A를 편집하여 문자열 B를 만들고자 함
# 세 연산 중 한번에 하나씩 선택하여 이용할 수 있음
# 1) 삽입 - 특정 위치에 하나의 문자 삽입 2) 삭제 - 특정 위치의 하나 문자 삭제 3) 교체 - 특정 위치 하나 문자 다른 문자로 교체

a=str(input())
b=str(input())

# 최소 편집 거리 계산을 위한 다이나믹 프로그래밍
def edit_dist(str1,str2):
    n=len(str1)
    m=len(str2)

    # 다이나믹 프로그래밍을 위한 2차원 dp 테이블 초기화
    dp=[[0]*(m+1) for _ in range(n+1)]

    # dp 테이블 초기 설정
    for i in range(1,n+1):
        dp[i][0]=i
    for j in range(1,m+1):
        dp[0][j]=j

    # 최소 편집 거리 계산
    for i in range(1,n+1):
        for j in range(1,m+1):

            # 문자가 같을 경우
            if str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            # 문자가 다를 경우, 왼쪽(삽입), 위쪽(삭제), 왼쪽 위(교체) 중 최소 비용을 찾아 대입하고 +1
            else:
                dp[i][j]=1+min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])

    return dp[n][m]

print(edit_dist(a,b))
