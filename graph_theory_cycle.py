# 서로소 집합을 활용한 사이클 판별

# 특정 원소가 속한 집합 찾기
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합 합치기
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a>b:
        parent[a]=b
    else:
        parent[b]=a

# 노드의 개수, 간선의 개수 입력 받기
v,e=map(int,input().split())
parent=[0]*(v+1)

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i]=i

# cycel 발생 여부
cycle=False

for i in range(e):
    a,b=map(int,input().split())
    # 사이클이 발생한 경우 종료
    if find_parent(parent,a)==find_parent(parent,b):
        cycle=True
        break
    else:
        union_parent(parent,a,b)

if cycle:
    print('사이클이 발생했습니다')
else:
    print('사이클이 발생하지 않았습니다')