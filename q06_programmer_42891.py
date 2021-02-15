# 무지의 먹방 라이브 - 그리디

import heapq

def solution(food_times,k):
    # 모든 음식을 먹는 시간의 합이 k보다 작거나 같다면 -1 return
    if sum(food_times)<=k:
        return -1

    # 시간이 작은 음식부터 빼야하므로 우선순위 큐를 이용함
    q=[]
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호)의 형태로 우선순위 큐에 삽입
        heapq.heappush(q,(food_times[i],i+1))
    # 음식을 먹는데 사용한 시간의 합
    sum_value=0
    # 이전 음식을 먹는데 걸린 시간
    previous=0
    # 남은 음식 개수
    length=len(food_times)

    while sum_value+((q[0][0]-previous)*length)<=k:
        # 뺄 음식의 시간
        now=heapq.heappop(q)[0]
        sum_value+=(now-previous)*length
        # 남은 음식 개수에서 다 먹은 음식은 빼줌
        length-=1
        # 이전 음식 시간 재설정
        previous=now

    # 남은 음식 중 몇번째 음식인지 확인하여 출력
    result=sorted(q,key=lambda x:x[1]) # 음식 번호 기준으로 정렬
    return result[(k-sum_value)%length][1]

print(solution([3,1,2],5))
