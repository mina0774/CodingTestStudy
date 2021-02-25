# 이진탐 - 가사 검색 (2020 카카오 신입 공채 1차)

from bisect import bisect_left,bisect_right

# 값이 [left_value,right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a,left_value,right_value):
    right_index=bisect_right(a,right_value)
    left_index=bisect_left(a,left_value)

    return right_index-left_index

# 모든 단어를 길이마다 나누어서 저장하기 위한 리스트
array=[[] for  _ in range(10001)]
# 모든 단어를 길이마다 나누어서 저장하기 위한 리스트
reversed_array=[[] for _ in range(10001)]

def solution(words,queries):
    answer=[]

    # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 삽입
    for word in words:
        array[len(word)].append(word)
        # 단어를 뒤집어서 삽입
        reversed_array[len(word)].append(word[::-1])

    for i in range(10001):
        array[i].sort()
        reversed_array[i].sort()

    for q in queries:
        if q[0]!='?':
            res=count_by_range(array[len(q)],q.replace('?','a'),q.replace('?','z'))
        else:
            res=count_by_range(reversed_array[len(q)],q[::-1].replace('?','a'),q[::-1].replace('?','x'))
        answer.append(res)
    return answer

print(solution(["frodo", "front", "frost", "frozen", "frame", "kakao"],["fro??", "????o", "fr???", "fro???", "pro?"]))