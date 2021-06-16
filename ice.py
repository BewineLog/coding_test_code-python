"""
-아이스크림 찾기
-N x M 의 얼음틀
-0: 구멍이 뚫린 곳, 1: 칸막이
-구멍이 뚫린 곳 기준 상/하/좌/우로 붙어 있는 경우, 서로 연결되어 있는 것으로 간주(1개로 count) -> 아이스크림
-값이 주어졌을 때, 아이스크림의 갯수를 구하시오.

-use DFS
"""

n,m = map(int,input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y) -> bool:
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    #현재 노드 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1 #방문 처리

        #방문 처리용 재귀함수(상/하/좌/우)
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False

#모든 노드에 대하여 음료수 채우기
result = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result += 1

print(result)




