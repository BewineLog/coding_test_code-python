import sys
import heapq


n,m,k,x = map(int, sys.stdin.readline().rstrip().split())
graph = [[] *(n+1) for _ in range(n+1)]

for _ in range(m):
    node1, node2 = map(int,sys.stdin.readline().rstrip().split())

    graph[node1].append(node2)

q = [(0,x)]

dist = [1E9] * (n+1)
dist[x] = 0

while q:
    cost, node = heapq.heappop(q)

    if dist[node] < cost: continue

    for i in graph[node]:
        newCost, newNode = 1, i

        distance = newCost + cost
        if dist[newNode] > distance:
            dist[newNode] = distance
            heapq.heappush(q,(distance,newNode))
        else:
            continue

if dist.count(k) == 0:
    print(-1)
else:
    for j in range(1,n+1):
        if dist[j] == k:
            print(j)
