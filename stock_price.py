def solution(prices):
    # 정답 배열 초기화
    answer = [0] * len(prices)
    # 이중 반복문을 사용해서 각각의 주식 가격을 비교
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            answer[i]+=1
            # 만약 현재 시점의 가격이 그 다음 시점의 가격보다 크다면 가격이 떨어진 것이므로
            # 바로 위의 for문을 빠져나감
            if prices[i]>prices[j]:
                break
    return answer

print(solution([1,2,3,2,3]))