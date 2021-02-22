# 그래프 이론 - 여행 계획

# 서로소 집합 알고리즘 이용
# 노드 간의 연결성 파악

# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

n,m=map(int,input().split())
parent=[0]*(n+1)

# 부모 테이블 상에서 부모 자기 자신을 초기화
for i in range(1,n+1):
    parent[i]=i

# union 연산 수행
for i in range(n):
    data=list(map(int,input().split()))
    for j in range(n):
        if data[j]==1:
            union_parent(parent,i+1,j+1)

# 계획 입력 받기
plan=list(map(int,input().split()))

result=True
# 여행 게획에 속하는 모든 루트의 노드가 동일한지 확인
for i in range(m-1):
    if find_parent(parent,plan[i])!=find_parent(parent,plan[i+1]):
        result=False

if result:
    print("YES")
else:
    print("NO")
