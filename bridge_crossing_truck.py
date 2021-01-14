def solution(bridge_length, weight, truck_weights):
    time = 0
    # 1초에 트럭은 1만큼 움직일 수 있으므로
    # 길을 건너고 있는 트럭을 나타내기 위해
    # 다리 길이만큼의 배열을 선언하여 각 위치에서 지나가고 있는 트럭을 표기하게끔 배열을 생성
    ontheway_truck = [0] * bridge_length

    # 길을 지나고 있는 트럭이 존재할 때 까지 반복문을 반복
    while ontheway_truck:
        # 시간이 1초 지나면
        time+=1
        # 다리에 0 인덱스에 위치한 트럭이 빠져야함
        ontheway_truck.pop(0)
        # 만약 대기하는 트럭이 존재한다면
        if truck_weights:
            # 현재 다리에 놓여있는 모든 트럭의 무게와 현재 대기트럭에서 들어올 트럭의 무게의 합이
            # 다리가 수용할 수 있는 무게보다 작거나 같다면
           if sum(ontheway_truck)+truck_weights[0]<=weight:
                # 현재 길을 지나고 있는 트럭의 배열에 이 값을 넣어줌
                ontheway_truck.append(truck_weights.pop(0))
            # 만약 무게가 더 크다면, 어떤 트럭도 들어올 수 없으므로
           else:
                # 현재 길을 지나고 있는 트럭의 배열에 0의 값을 넣어줌
                ontheway_truck.append(0)

    return time

print(solution(2,10,[7,4,5,6]))