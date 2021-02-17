# 정렬 - 안테나 백준 18310
n=int(input())
data=list(map(int,input().split()))
data.sort()

print(data[n//2-1])