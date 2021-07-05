"""
-도시 분할 계획

-N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있다.
-길 마다 길을 유지하는 비용이 들어간다.

-마을을 2개로 분리, 각 분리된 마을 안에 집들이 서로 연결되도록 분할 하여야 한다. (각 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야 한다.)
-마을에는 집이 하나 이상 존재하여야 한다.

-최소한의 길과 최소 비용으로 구현하고자 한다.
"""
import sys

def find_parent(parent,x):
    if parent[x] != x:
        parent[x] = find_parent(parent,parent[x])
    return parent[x]

def union_parent(parent,a,b):
    a = find_parent(parent,a)
    b = find_parent(parent,b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n,m = map(int,input().split())  # 집의 개수, 길의 개수

parent = [0] * (n+1)
edges = []

for i in range(1,n+1):
    parent[i] = i

for _ in range(m):
    a,b,c = map(int,sys.stdin.readline().split()) # a -> b // cost: c
    edges.append((c,a,b))

edges.sort()
last = 0    # 최소 신장 트리에 포함되는 간선중 제일 비용이 큰 간선
result = 0  # cost 합

for edge in edges:
    cost,a,b = edge
    if find_parent(parent,a) != find_parent(parent,b):
        union_parent(parent,a,b)
        result += cost
        last = cost

print(result - last)
