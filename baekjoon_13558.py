# 백준 13558 - 등차수열의 개수

'''
길이가 N인 수열 A1, A2, ..., AN이 주어진다.
이때, 1 ≤ i < j < k ≤ N 이면서, Aj - Ai = Ak - Aj를 만족하는 (i, j, k) 쌍의 개수를 구하는 프로그램을 작성하시오.
즉 Ai+Ak=2Aj

<입력>
첫째 줄에 수열의 크기 N (3 ≤ N ≤ 100,000)가 주어진다.
둘째 줄에는 A1, A2, ..., AN이 주어진다. (1 ≤ Ai ≤ 30,000)

<출력>
1 ≤ i < j < k ≤ N 이면서, Aj - Ai = Ak - Aj를 만족하는 (i, j, k) 쌍의 개수를 출력한다.
'''

# 메모리 초과나는 풀이
from itertools import combinations

n=int(input())
array=list(map(int,input().split()))

items=[]
for i in range(n):
    items.append(i)

combs=list(combinations(items,3))
result=0
for comb in combs:
    i,j,k=comb
    if array[i]+array[k]==2*array[j]:
        result+=1
print(result)