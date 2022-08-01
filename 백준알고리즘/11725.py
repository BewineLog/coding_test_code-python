import sys
import heapq

n = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int,sys.stdin.readline().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)

data = []
visited = [False] * (n+1)

def bfs():
    q = [1]
    visited[1] = True
    while q:
        node = heapq.heappop(q)
        for i in graph[node]:
            if not visited[i]:
                visited[i] = True
                heapq.heappush(data,(i,node))
                heapq.heappush(q,i)

bfs()

while data:
    print(heapq.heappop(data)[1])
