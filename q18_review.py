# bfs/dfs 괄호변환 (2020 카카오 신입 공채 1차)

# ( 개수, ) 개수 같으면 균형잡힌 문자열
# ( ) 짝도 맞으면 올바른 괄호 문자열

# 1) 균형잡힌 괄호 문자열은 개수만 파악
#  1-1) 균형잡힌 괄호 문자열이라면
#      올바른 괄호 문자열 평가 -> 입력이 빈 문자열인 경우, 빈 문자열 반환
#                        -> 문자열 w를 두 균형잡힌 문자열 u,v로 분리 (u는 균형잡힌 괄호 문자열로 더 이상 분리할 수 없음, v는 빈 문자열이 될 수 있음)
#                        -> 수행한 결과 문자열을 u에 이어 붙인 후 반환
#                           -> u가 올바른 괄호 문자열이면 문자열 v에 대해 다시 1단계부터 수행
#                        -> u가 올바른 괄호 문자열이 아니라면
#                           -> 빈 문자열에 첫번째 문자로 (를 붙임
#                           -> 문자열 v에 대해 1단계부터 재귀적으로 수행한 결과 문자열을 이어 붙임
#                           -> )를 다시 붙임
#                           -> u의 첫번째 문자, 마지막 문자 제거, 나머지 문자열의 괄호 방향을 뒤집어서 붙임
#                           -> 생성된 문자열 반환

def balanced_index(s):
    cnt=0

    for i in range(len(s)):
        if s[i]=='(':
            cnt+=1
        else:
            cnt-=1

        if cnt==0:
            return i

def isCorrect(s):
    count=0
    for i in s:
        if i == '(':
            count+=1
        else:
            if count == 0:
                return False
            count-=1

    if count==0:
        return True

def solution(p):
    answer=""
    if p=="":
        return answer

    index=balanced_index(p)
    u=p[:index+1]
    v=p[index+1:]

    # 올바른 괄호 문자열이라면
    if isCorrect(u):
        answer=u+solution(v)
    else:
        answer='('
        answer+=solution(v)
        answer+=')'
        u=list(u[1:-1]) # 첫 문자와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i]=='(':
                u[i]=')'
            else:
                u[i]='('
        answer+="".join(u)

    return answer

print(solution("()))((()"))

