import sys
import heapq

INF =1e9

v,e = map(int,sys.stdin.readline().split())

k = int(input())

graph = [[]for _ in range(v+1)]

dist = [INF] * (v+1)
dist[k] = 0

for _ in range(e):
    start, end, cost= map(int,sys.stdin.readline().split())
    graph[start].append((cost,end))

def dijkstra(k):
    queue = []
    heapq.heappush(queue,(0,k))

    while queue:
        cost,node = heapq.heappop(queue)

        for nextCost,nextNode in graph[node]:
            distance = dist[node] + nextCost
            if distance < dist[nextNode]:
                dist[nextNode] = distance
                heapq.heappush(queue,(distance,nextNode))

dijkstra(k)

for i in range(1,v+1):
    if dist[i] == INF:
        print('INF')
    else:
        print(dist[i])
