import sys
import heapq
MAX = 10001

n,d = map(int,sys.stdin.readline().rstrip().split())

road = [[]*(MAX) for _ in range(MAX)]
heap = []
dist = [i for i in range(MAX)]

for _ in range(n):
    start, end, cost = map(int,sys.stdin.readline().rstrip().split())
    heapq.heappush(heap,(end,start,cost))

while heap:
    newEnd, newStart, newCost = heapq.heappop(heap)

    if newCost > (dist[newEnd] - dist[newStart]) or newEnd > d:
        continue

    distance = dist[newStart] + newCost

    if dist[newEnd] > distance:
        dist[newEnd] = distance

    for i in range(newEnd+1,MAX):
        dist[i] = min(dist[i],dist[i-1]+1)

print(dist[d])
