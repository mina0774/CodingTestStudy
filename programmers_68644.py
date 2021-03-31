# 두개뽑아서 더하기
from itertools import combinations
def solution(numbers):
    answer = []
    set_answer=set()
    array=list(combinations(numbers,2))
    for a in array:
        set_answer.add(a[0]+a[1])
    answer=list(set_answer)
    answer.sort()

    return answer

print(solution([2,1,3,4,1]))