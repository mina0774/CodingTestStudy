# 도시 분할 계획

# 최소 신장 트리를 만든 다음에 최소 신장 트리를 구성하는 간선 중에 가장 비용이 큰 간선을 제거하면
# 최소 신장 트리가 2개의 부분 그래프로 나누어짐!

def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

# 노드 개수, 간선 개수 입력 받기
v,e=map(int,input().split())
parent=[0]*(v+1)

# 모든 간선을 담을 리스트, 최종 비용을 담을 변수
edges=[]
result=0

# 부모 테이블상, 부모를 자기 자신으로 초기화
for i in range(1,v+1):
    parent[i]=i

# 모든 간선에 대한 정보 입력 받기
for _ in range(e):
    a,b,cost=map(int,input().split())
    edges.append((cost,a,b))

# 간선을 비용 순으로 정렬
edges.sort()
# 최소 신장 트리에 포함되는 간선 중 가장 비용이 큰 간선
last=0

for edge in edges:
    cost,a,b=edge
    # 사이클이 발생하지 않는 경우에만 집합 포함
    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost
        last=cost

print(result-last)