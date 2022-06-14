"""
-알고리즘 대회 출제 문제

-N개의 도시 존재, 각 도시는 보내고자 하는 메시지가 있는 경우 전보를 통해 전송 가능
-전보를 보내고자 한다면, 목적지로 향하는 통로가 설치되어 있어야 한다.

-특정 도시에서 최대한 많은 도시로 메세지를 보내고자 할 때, 각 도시의 번호와 통로의 정보를 통해 c에서 보낸 메세지를 받을 도시의 총 갯수와  총 걸리는 시간을 구하시오.
"""
import heapq
import sys

INF = int(1e9)

n, m, c = map(int, input().split())   # 도시의 갯수, 통로의 갯수, 메시지를 보내고자 하는 도시

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int,sys.stdin.readline().split())   # x->y 일 때, cost = z
    graph[x].append((y,z))

def dijkstra(start: int):
    q = []
    distance[start] = 0

    heapq.heappush(q,(0,start)) # cost, dst

    while q:
        dist,now = heapq.heappop(q)

        if distance[now] < dist: #이미 처리된 노드인 경우
            continue

        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q,(cost,i[0]))

dijkstra(c)

count = int(0)
time = int(0)

for d in distance:
    if d != INF:
        count += 1
        time += d

print(count-1,time)

