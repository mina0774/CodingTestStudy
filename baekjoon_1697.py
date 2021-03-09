# 백준 1697 그래프 알고리즘 숨바꼭질

'''
수빈이는 동생과 숨바꼭질을 하고 있다. 수빈이는 현재 점 N(0 ≤ N ≤ 100,000)에 있고, 동생은 점 K(0 ≤ K ≤ 100,000)에 있다.
수빈이는 걷거나 순간이동을 할 수 있다. 만약, 수빈이의 위치가 X일 때 걷는다면 1초 후에 X-1 또는 X+1로 이동하게 된다.
순간이동을 하는 경우에는 1초 후에 2*X의 위치로 이동하게 된다.
수빈이와 동생의 위치가 주어졌을 때, 수빈이가 동생을 찾을 수 있는 가장 빠른 시간이 몇 초 후인지 구하는 프로그램을 작성하시오.
'''

# bfs 처음 시작점 N에서 N*2, N-1, N+1로 이동 가능
# 이동 가능한 세 점 bfs 이용하여 모두 탐색해 K와 같을 때 찾기

from collections import deque

def bfs(visited,v,k):
    q=deque([v])

    while q:
        x=q.popleft()

        if x==k:
            return visited[x]

        for nx in [x+1,x-1,2*x]:
            # nx가 범위 안에 있고 방문하지 않은 노드일 경우
            if 0<=nx<100001 and visited[nx]==0:
                visited[nx]=visited[x]+1
                q.append(nx)

n,k=map(int,input().split())
visited=[0]*100001 # 해당 위치에 도달했을 때 몆 초 인지 저장할 배열

print(bfs(visited,n,k))





