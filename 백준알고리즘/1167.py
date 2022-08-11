import random
import sys
import heapq

n = int(input())

graph = [[] for _ in range(n+1)]
dist = [1E9] * (n+1)

for i in range(1,n+1):
    line = list(map(int,sys.stdin.readline().rstrip().split()))
    nowNode = line[0]

    for j in range(1,len(line)-1,2):
        graph[nowNode].append((line[j+1], line[j])) #cost, nextNode

def dijkstra(node):
    q = [(0,node)]

    while q:
        startCost, startNode = heapq.heappop(q)

        for nextCost,nextNode in graph[startNode]:
            distance = dist[startNode] + nextCost

            if dist[nextNode] > distance:
                dist[nextNode] = distance
                heapq.heappush(q,(distance,nextNode))

#임의의 점으로 부터 제일 먼 노드 X 구하기
startpos = random.randint(1,n)
dist[startpos] = 0
dijkstra(startpos)
index = dist.index(max(dist[1:]))

#X로부터 제일 먼 노드 Y 구하기
dist = [1E9] * (n+1)
dist[index] = 0
dijkstra(index)

#X-Y의 거리가 지름이 된다
print(max(dist[1:]))
