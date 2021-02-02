# 최소 신장 트리 알고리즘 = 크루스칼 알고리즘
# 신장 트리란? 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a>b:
        parent[a]=b
    else:
        parent[b]=a

v,e=map(int,input().split())
parent=[0]*(v+1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges=[]
result=0

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i]=i

# 모든 간선에 대한 정보를 입력받기
for _ in range(e):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))

# 간선을 비용 순으로 정렬
edges.sort()

for edge in edges:
    cost,a,b=edge
    # 사이클이 발생하지 않는 경우 집합에 포함
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost

print(result)