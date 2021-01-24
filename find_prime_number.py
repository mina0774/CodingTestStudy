from itertools import permutations
import math

# 소수인지 아닌지 판정하는 함수
def check(n):
    k=math.sqrt(n)

    if n<2:
        return False

    for i in range(2,int(k)+1):
        if n%i==0:
            return False
        return True

def solution(numbers):
    answer=[]

    for k in range(1,len(numbers)+1):
        # 순열을 이용하여 카드로 만들 수 있는 모든 조합의 숫자 배열을 생성
        perlist=list(map(''.join,permutations(list(numbers),k)))

        # 중복 제거를 위하여 set함수를 이용
        for i in set(perlist):
            # 자릿수가 다를 때 중복이 발생할 수도 있으니
            # 소수가 되는 모든 조합을 answer 배열에 넣은 후
            if check(int(i)):
                answer.append(int(i))
        # 중복 제거를 위한 set 처리 후 그결과를 반환
    return len(set(answer))

print(solution("011"))