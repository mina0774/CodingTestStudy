# 카카오 블라인드 - 메뉴 리뉴얼

# collections의 Counter 사용법
# Counter(temp) 할 경우 -> temp가 배열일 , 각 temp에 "AB" "BC" "CD" "AB" 이렇게 원소를 가지고 있다고 하면
# Counter(temp)의 값은 [("AB",2),("BC",1),("CD",1)]이 됨

from itertools import combinations
from collections import Counter

def solution(orders,course):
    answer=[]
    for i in course:
        temp=[]
        # 손님이 주문한 주문들을 반복을 해준 후
        for order in orders:
            # 현재의 courser수 만큼의 조합을 생성하여
            comb=combinations(sorted(order),i)
            # temp 배열에 모두 넣어준
            temp+=comb
        # temp 배열에 있는 각각의 원소의 개수를 counter해줌
        counter=Counter(temp)

        # counter의 길이가 0이 아니고, max값이 2 이상일 경우
        if len(counter)!=0 and max(counter.values())!=1:
            # counter의 값을 모두 반복해주면서
            for a in counter:
                # 현재의 값이 counter의 최대값일 때
                if counter[a]==max(counter.values()):
                # 정답 배열에 넣어줌
                    answer.append("".join(a))

    return sorted(answer)