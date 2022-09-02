import sys
import heapq

MAX = 100001
n,k = map(int,sys.stdin.readline().rstrip().split())


distance = [1e9] * MAX
visited = [False] * MAX
distance[n] = 0

q = [[0,n]]

def dijkstra():
    while q:
        nowCost, nowNode = heapq.heappop(q)
        visited[nowNode] = True

        if nowNode == k:
            break

        move = [[nowCost, nowNode*2], [nowCost + 1, nowNode - 1], [nowCost+1, nowNode+1]]

        for i in range(3):

            if move[i][1] >= MAX or move[i][1] < 0 or visited[move[i][1]]:
                continue

            if distance[move[i][1]] > move[i][0]:
                distance[move[i][1]] = move[i][0]
                heapq.heappush(q,move[i])


dijkstra()
print(distance[k])
