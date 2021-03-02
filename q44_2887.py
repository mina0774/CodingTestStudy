# 그래프 이론 문제 - 행성 터널 (백준 2887)
# 크루스칼 알고리즘 이용하기
# N개의 행성
# 3차원 좌표계
# 터널 연결 N-1개
# 터널 연결 최소 비용

# 특정 원소가 속한 집합을 찾기
def find_parent(parent,x):
    if parent[x]!=x:
        parent[x]=find_parent(parent,parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent,a,b):
    a=find_parent(parent,a)
    b=find_parent(parent,b)

    if a>b:
        parent[a]=b
    else:
        parent[b]=a

n=int(input())
parent=[0]*(n+1)

# 모든 간선을 담을 리스트와 최종 비용을 담을 변수
edges=[]
result=0

# 부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1,n+1):
    parent[i]=i

x=[]
y=[]
z=[]

# 모든 노드에 대한 좌표값 입력받기
for i in range(1,n+1):
    data=list(map(int,input().split()))
    x.append((data[0],i))
    y.append((data[1],i))
    z.append((data[2],i))

x.sort()
y.sort()
z.sort()

for i in range(n-1):
    edges.append((x[i + 1][0] - x[i][0], x[i + 1][1], x[i][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i + 1][1], y[i][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i + 1][1], z[i][1]))

edges.sort()

for edge in edges:
    cost,a,b=edge

    if find_parent(parent,a)!=find_parent(parent,b):
        union_parent(parent,a,b)
        result+=cost

print(result)