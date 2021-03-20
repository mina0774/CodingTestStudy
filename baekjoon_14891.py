# 백준 14891 - 톱니바퀴
# 극이 다를 때만 반대방향으로 회전
# 극이 같으면 회전 X

# 1은 시계방향
# -1은 반시계방향


# deque rotate 함수 이용 -> 양수면 오른쪽, 음수면 왼쪽

from collections import deque

array=[]
for _ in range(4):
    array.append(deque(map(int,input())))
k=int(input())
for _ in range(k):
    num,dir=map(int,input().split())
    num-=1 # index는 0부터 시작

    # 비교대상
    temp2=array[num][2]
    temp6=array[num][6]

    # 시작 톱니를 돌려줌
    array[num].rotate(dir)
    temp_dir=dir

    # 시작톱니 오른쪽 방향
    dir=temp_dir
    for i in range(num+1,4):
        if array[i][6]!=temp2:
            temp2=array[i][2]
            dir *= -1
            array[i].rotate(dir)
        else:
            break

    # 시작톱니 왼쪽 방향
    dir=temp_dir
    for i in range(num-1,0-1,-1):
        if array[i][2]!=temp6:
            temp6=array[i][6]
            dir*=-1
            array[i].rotate(dir)
        else:
            break

ans=0
for i in range(4):
    if array[i][0]==1:
        ans+=(2**i)
print(ans)