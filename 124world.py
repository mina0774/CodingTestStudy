# 규칙을 찾아야하는 문제 
# 나머지가 1일 때 -> 1
# 나머지가 2일 때 -> 2
# 나머지가 0일 때 -> 4로 표기, 나머지가 0일 때는 n의 값을 1 감소 시켜주어야 함
def solution(n):
    answer = ''

    dict = {1: '1', 2: '2', 0: '4'}

    while n > 0:
        a = n % 3
        n = n // 3

        if (a == 0):
            n -= 1

        answer = dict[a] + answer

    return answer

print(solution(4))