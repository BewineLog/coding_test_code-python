import sys

INF = sys.maxsize

n = int(input())    # number of city
m = int(input())    # number of bus

graph = [[INF] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        if i == j:
            graph[i][j] = 0  # path to self = 0

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(graph[a][b],c)    # update array about initial path

# D_ab = D_ak + D_kb
for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1,n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            graph[i][j] = 0
for i in range(1, n+1):
    print(*graph[i][1:])
    # print(' '.join(map(str,graph[i][1:])))
