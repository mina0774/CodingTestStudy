from collections import deque

# 도시 개수, 도로 개수, 최단 거리, 시작점
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

# 각 노드의 거리를 저장하는 배열
distance = [-1] * (n + 1)
# 출발지에서의 거리는 0으로 설정
distance[x] = 0

queue = deque([x])

while queue:
    v = queue.popleft()
    for i in graph[v]:
        if distance[i] == -1:
            queue.append(i)
            distance[i] = distance[v] + 1

# 최단거리가 k인 도시가 존재하지 않을 경우 사용하는 check 변수
check = False
for i in range(len(distance)):
    if distance[i] == k:
        check = True
        print(i, end=' ')

if check == False:
    print(-1)