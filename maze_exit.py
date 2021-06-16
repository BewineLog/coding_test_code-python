"""
-미로 탈출
-NxM
-시작점 : (1,1), 출구 (N,M)
-한번에 한칸씩 이동 가능
-1: 괴물이 없는 부분, 0: 괴물이 있는 부분
-미로는 반드시 탈출할 수 있는 형태
-> 탈출을 위해 움직여야 하는 최소 칸 수를 구하여라.
-> use BFS (노드에서 가장 가까운 노드부터 탐색하기 때문)
"""
from collections import deque

n,m = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,input())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):

    queue = deque()
    queue.append((x,y))

    while queue:
        x,y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1 #값을 누적
                queue.append((nx,ny))
            else:
                continue

    return graph[n-1][m-1]


print(bfs(0,0))








