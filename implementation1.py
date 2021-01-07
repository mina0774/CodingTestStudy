n=int(input())
plans=input().split()
x,y=1,1

# 방향에 따라 좌표의 변화값 설정
dx=[0,0,-1,1]
dy=[-1,1,0,0]
dir=['L','R','U','D']

# plan을 반복
for plan in plans:
    # 해당 plan의 방향이 dir 방향 배열을 탐색해서 해당하는 dir 배열 원소가 나오면
    # 좌표를 옮겨
    for i in range(len(dir)):
        if plan==dir[i]:
            nx=x+dx[i]
            ny=y+dy[i]
    # 좌표를 옮겼을 때, 범위 바깥으로 벗어난다면
    if nx>n or ny>n or nx<1 or ny<1:
        # 무시하고 다시 for문으로 돌아감
        continue

    x,y=nx,ny

print(x,y)