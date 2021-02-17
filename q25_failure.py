# 정렬 - 실패율 42889 (2019 카카오 신입 공채 1차)
def solution(N,stages):
    answer=[]
    length=len(stages)

    for i in range(1,N+1):
        count=stages.count(i)

        if length==0:
            fail=0
        else:
            fail=count/length

        length-=count
        answer.append((i,fail))

    answer=sorted(answer,key=lambda x:x[1],reverse=True)
    answer=[i[0] for i in answer]

    return answer

print(solution(5,[2,1,2,6,2,4,3,3]))