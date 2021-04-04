# 백준 1561 놀이공원 - binary search

n,m=map(int,input().split())
time_list=list(map(int,input().split()))

# 마지막 아이가 타기 직전까지의 시간과 그때 까지 몇명이 탔는지 계산하기
first,last=0,n*max(time_list)
max_cnt,max_min=0,0
while first<=last:
    mid=(first+last)//2
    cnt=sum([(mid-1)//time +1 for time in time_list])

    if cnt<n:
        first=mid+1
        max_cnt=cnt
        max_min=mid
    else:
        last=mid-1

for i,time in enumerate(time_list):
    if max_min%time==0:
        max_cnt+=1
        if max_cnt==n:
            print(i+1)
            break
