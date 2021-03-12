# programmers - 정렬 문제 (h-index)
# enumerate는 index와 value를 같이 반환해주는 함수

def solution(citations):
    answer = 0
    citations.sort(reverse=True)

    # enumerate는 index와 value를 같이 반환해줌
    for i, value in enumerate(citations):
        if i >= value:
            return i
    return len(citations)

print(solution([3, 0, 6, 1, 5]))