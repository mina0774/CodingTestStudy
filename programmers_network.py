# 프로그래머스 - 네트워크
# bfs/dfs 관련 개념


def dfs(v, visited, graph):
    visited[v] = True

    for i in graph[v]:
        if not visited[i]:
            dfs(i, visited, graph)


def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [False] * (n + 1)

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i].append(j)
                graph[j].append(i)

    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(i, visited, graph)
            count += 1

    return count