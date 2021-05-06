from collections import defaultdict

def solution(gems):
    gdict=defaultdict(int)
    gnum=len(set(gems))

    left=0
    right=0
    answer=[0,len(gems)]

    while right<len(gems):
        gdict[gems[right]]+=1
        right+=1

        if len(gdict)==gnum:
            while left<right:
                if gdict[gems[left]]<=1:
                    break
                gdict[gems[left]]-=1
                left+=1

            if answer[1]-answer[0]+1>right-left:
                answer=[left+1,right]

    return answer

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))