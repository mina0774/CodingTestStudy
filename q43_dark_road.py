# 그래프 이론 문제 - 어두운 길 (크루스칼 - 최소신장트리)

# n개의 집 (0~n-1번), m개의 도로

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

n,m=map(int,input().split())
edges=[]
parent=[0]*(n+1)
for i in range(1,n+1):
    parent[i]=i

for _ in range(m):
    a,b,dist=map(int,input().split())
    edges.append((dist,a,b))

edges.sort()

result=0
for edge in edges:
    if find_parent(parent,edge[1])!=find_parent(parent,edge[2]):
        # 사이클 발생하지 않으므로
        union_parent(parent,edge[1],edge[2])
    else:
        result+=edge[0]
print(result)


