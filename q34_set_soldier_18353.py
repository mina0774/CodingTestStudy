# 다이나믹 프로그래밍 - 병사 배치하기 (백준 18353)

# 가장 긴 증가하는 부분 수열 문제
# D=[1,1,1,..] D는 array[i]를 마지막 원소로 가지는 부분 수열의 최대 길이인데
# 이 문제는 내림차순으로 가장 긴 순열을 뽑으면 가장 긴 감소하는 부분 수열 문제라고 생각하면
# if문 부등호를 반대로만 해주면 됨
# 0<=j<i D[i]=max(D[i],D[j]+1) if array[j]>array[i]

n=int(input())
array=list(map(int,input().split()))

D=[1]*n

for i in range(1,n):
    for j in range(i):
        if array[j]>array[i]:
            D[i]=max(D[i],D[j]+1)

print(n-max(D))