# 한 번 계산된 결과를 메모제이션(memoization)하기 위한 리스트 초기화
# 탑다운 방식 (하향식)
d=[0]*100

# 피보나치 함수를 재귀함수로 구현 (탑다운 다이나믹 프로그래밍)
def fibo(x):
    if x==1 or x==2:
        return 1

    # 이미 계산한 적이 있는 항이라면 그대로 반환
    if d[x]!=0:
        return d[x]

    d[x]=fibo(x-1)+fibo(x-2)

    return d[x]

print(fibo(99))