import sys
from collections import deque
sys.setrecursionlimit(10000)

n,m = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b= map(int,sys.stdin.readline().split())

    graph[a].append(b)
    graph[b].append(a)

visited = [False]*(n+1)
group = 0
def dfs(x):
    visited[x] = True

    for i in graph[x]:
        if visited[i] == False:
            dfs(i)

for i in range(1,n+1):
    if visited[i] == False:
        dfs(i)
        group+=1

print(group)
