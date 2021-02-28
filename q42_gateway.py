# 그래프 이론 - 탑승구 (서로소 집합 알고리즘 이용)

# G개의 탑승구 (1-G번)
# P개의 비행기

# 도킹하는 과정을 탑승구 간 합집합 연산으로 이해
# 새로운 비행기가 도킹되면, 해당 집합을 바로 왼쪽에 있는 집합과 합침
# 단, 집합의 루트가 0이면 더 이상 도킹 불가

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

g=int(input())
p=int(input())

parent=[0]*(g+1)
for i in range(1,g+1):
    parent[i]=i

result=0
for _ in range(p):
    data=find_parent(parent,int(input()))

    if data==0:
        break
    else:
        union_parent(parent,data,data-1)
        result+=1

print(result)
