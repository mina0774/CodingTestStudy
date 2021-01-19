def solution(n):
    answer = []
    # 저장 예시
    # n=4일 때
    # 1 0 0 0
    # 2 9 0 0
    # 3 10 8 0
    # 4 5 6 7
    # 이렇게 저장하는 배열을 만들 공간을 만들어줌
    res = [[0] * n for _ in range(n)]
    num = 1

    # 방향은 down부터 시작하므로 x의 초기값을 -1로 지정해주어야 함
    x = -1
    y = 0

    # 이 문제는 규칙을 찾는 것이 가장 중요한데,
    # n=4일 경우의 예시를 들어보면
    # 먼저 위와 같이 배열을 저장하려면
    # [1] 1,2,3,4 일 때는 움직이는 방향이 down이므로 x값을 1 증가
    # [2] 5,6,7 일 때는 움직이는 방향이 right이므로 y값을 1 증가
    # [3] 8,9 일 때는 움직이는 방향이 up이므로 x값, y값을 1씩 감소
    # [4] 10 일 때는 움직이는 방향이 down이므로 x값을 1 증가
    # 이 과정을 살펴보면 반복문이 도는 횟수는 4,3,2,1로 줄어드는 것을 확인할 수 있음
    # 그러면 이중 for문을 작성하여
    # 먼저 for문을 써서 range(n)으로 한 바퀴를 돌려주고
    # 그 안에 for문을 한번 더 써서 range(i,n)까지 한 바퀴를 돌려주면
    # 4,3,2,1의 횟수로 안에 있는 for문이 반복된다.
    # 또한 숫자가 이동하는 방향은 down,right,up 순으로 반복되므로
    # i%3==0이면 down / ==1이면 right / ==2이면 up
    for i in range(n):
        for j in range(i, n):

            # down
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1

            res[x][y] = num
            num += 1

    for i in range(n):
        for j in range(n):
            if res[i][j] != 0:
                answer.append(res[i][j])

    return answer

print(solution(10))