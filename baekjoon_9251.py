# 백준 LCS - 9251 (다이나믹 프로그래밍)

'''
<문제>
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

<입력>
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

<출력>
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.
'''

import sys

a=' '+sys.stdin.readline().strip()
b=' '+sys.stdin.readline().strip()

dp=[[0]*len(b) for _ in range(len(a))]

for i in range(1,len(a)):
    for j in range(1,len(b)):
        if a[i]==b[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i][j-1],dp[i-1][j])

print(dp[-1][-1])