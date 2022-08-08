import sys
import heapq

n = int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    startNode, endNode, cost = map(int,sys.stdin.readline().rstrip().split())

    graph[startNode].append((cost,endNode))

start, end = map(int,sys.stdin.readline().rstrip().split())

q = [(0,start)]
route = [[] for _ in range(n+1)]
distance = [1E9] * (n+1)
distance[start] = 0

while q:
    cost, node = heapq.heappop(q)

    if cost > distance[node]:
        continue
    for newCost, newNode in graph[node]:
        dist = newCost + distance[node]
        if dist < distance[newNode]:
            distance[newNode] = dist
            route[newNode] = [node]
            heapq.heappush(q,(distance[newNode],newNode))

pos = end
minRoute = [end]
while pos != start:
    minRoute.append(route[pos][0])
    pos = route[pos][0]

print(distance[end])
print(len(minRoute))
for i in minRoute[::-1]:
    print(i,end =' ')
