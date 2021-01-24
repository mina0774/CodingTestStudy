# 개미전사

# 일직선으로 이어져있는 식량창고를 약탈하기 위해서 최소한 한 칸 이상 떨어진 식량창고를 약탈해야 함
# 식량의 최댓값을 구하는 프로그램

# 정수 N을 입력받기4
n=int(input())
# 모든 식량 정보 입력 받기
array=list(map(int,input().split()))

# 계산된 결과 저장 위한 DP 테이블 초기화
d=[0]*100

# 다이나믹 프로그래밍 진행(보텀업)
d[0]=array[0]
d[1]=max(array[0],array[1])

for i in range(2,n):
    d[i]=max(d[i-1],d[i-2]+array[i])

print(d[n-1])