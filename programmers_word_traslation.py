# 프로그래머스 단어 변환 (dfs/bfs) 유형

# bfs - 너비 우선 탐색 이용

# 우선 한 문자만 다른지 확인해주는 함수
from collections import deque
def IsDiffOneChar(a,b,n):
    cnt=0

    for i in range(n):
        if a[i]!=b[i]:
            cnt+=1
    if cnt==1:
        return True
    else:
        return False

def solution(begin,target,words):
    answer=0

    visited=dict()
    len_word=len(begin)
    q=deque([(begin,0)])
    visited[begin]=True

    while q:
        now,step=q.popleft()

        for word in words:
            if IsDiffOneChar(now,word,len_word) and word not in visited:
                visited[word]=True
                q.append((word,step+1))
                if word == target:
                    answer = step + 1
    return answer

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))