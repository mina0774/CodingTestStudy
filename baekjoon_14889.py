# 스타트와 링크
# Brute Force Algo
from itertools import combinations

n=int(input())
ability=[]
members=[i for i in range(n)]

for _ in range(n):
    ability.append(list(map(int,input().split())))

# 조합으로 가능한 팀 생성
possible_team=[]

'''
0~n까지 조합을 생성하여 리스트에 담으면 첫 조합의 여집합은 마지막 조합이다.
즉 team[i] 는 team[-i-1]과 완전히 반대된다. 이를 이용하여 풀면 쉽다.
'''
for team in list(combinations(members,n//2)):
    possible_team.append(team)


min_score=100000
for i in range(len(possible_team)//2):
    teamA=possible_team[i]
    teamB=possible_team[-i-1]

    scoreA=0
    scoreB=0

    for j in range(n//2):
        memberA=teamA[j]
        memberB=teamB[j]

        for A in teamA:
            scoreA+=ability[memberA][A]

        for B in teamB:
            scoreB+=ability[memberB][B]

    min_score=min(min_score,abs(scoreA-scoreB))

print(min_score)

