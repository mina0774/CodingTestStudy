# 다이나믹 프로그래밍 - 금광
t=int(input())

for _ in range(t):

    n,m=map(int,input().split())
    array=list(map(int,input().split()))

    # 다이나믹 프로그래밍을 위한 2차원 테이블 초기화
    dp=[]
    index=0
    for i in range(n):
        dp.append(array[index:index+m])
        index+=m

    # 다이나믹 프로그래밍 실행
    for j in range(1,m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i==0:
                # 첫번째 행일 때 왼쪽 위에서 오는 경우는 없으므로
                left_up=0
            else:
                left_up=dp[i-1][j-1]

            # 왼쪽 아래에서 오는 경우
            if i==n-1:
                # 마지막 행일 때 왼쪽 아래에서 오는 경우는 없으므로
                left_down=0
            else:
                left_down=dp[i+1][j-1]

            # 왼쪽에서 오는 경우
            left=dp[i][j-1]

            dp[i][j]=dp[i][j]+max(left_up,left_down,left)

    result=0
    for i in range(n):
        result=max(result,dp[i][m-1])

    print(result)


