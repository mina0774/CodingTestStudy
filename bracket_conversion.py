# 괄호 변환

# 균형잡힌 괄호 문자열인지 확인하는 함수
def isBalanced(s):
    chk=0
    for i in s:
        if i=='(': chk+=1
        elif i==')': chk-=1

    if chk==0: return True
    else: return False

# 올바른 괄호 문자열인지 확인하는 함수
def isCorrect(s):
    stack=[]
    stack.append(s[0])

    for i in range(1,len(s)):
        if len(stack)==0 or stack[-1]==')' or (stack[-1]=='(' and s[i]=='('):
            stack.append(s[i])
        else:
            stack.pop()

    if len(stack)==0:
        return True
    else:
        return False

def solution(p):
    answer = ''
    u=''
    v=''

    # 빈 문자열이거나 올바른 문자열이면 그대로 반환해줌
    if len(p)==0 or isCorrect(p): return p

    # u가 균형잡힌 문자열이 될 때까지 2개씩 추가해서 u,v 나누기
    for i in range(2,len(p)+1,2):
        if isBalanced(p[0:i]):
            u=p[0:i]
            v=p[i:len(p)]
            break

    # u가 올바른 괄호 문자열이라면
    if isCorrect(u):
        answer+=u+solution(v)
    # u가 올바른 괄호 문자열이 아니라면
    else:
        answer+='('+solution(v)+')'
        for c in u[1:-1]:
            if c=='(': answer+=')'
            else: answer+='('

    return answer

print(solution("()))((()"))