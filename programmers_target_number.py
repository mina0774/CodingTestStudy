# 타겟넘버 (bfs/dfs 둘 다로 풀어보기)

# dfs 풀이

answer=0
def dfs(numbers,target,i):
    global answer
    if i==len(numbers):
        if sum(numbers)==target:
            answer+=1
            return
    else:
        dfs(numbers,target,i+1)
        numbers[i]*=-1
        dfs(numbers,target,i+1)

def solution(numbers,target):
    global answer

    dfs(numbers,target,0)

    return answer

print(solution([1,1,1,1,1],3))



# bfs 풀이
from collections import deque


def solution(numbers, target):
    answer = 0
    q = deque([(0, 0)])

    while q:
        current_sum, index = q.popleft()

        if index == len(numbers):
            if current_sum == target:
                answer += 1
        else:
            num = numbers[index]
            q.append((current_sum + num, index + 1))
            q.append((current_sum - num, index + 1))

    return answer

print(solution([1,1,1,1,1],3))