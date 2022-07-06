import sys
from collections import deque

sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())

array = [[]*n for _ in range(n)]
for i in range(n):
    array[i] = list(sys.stdin.readline().strip())

cnt = 0
visited = [[False]*n for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
def bfs_blind(a,b,color):

    q = deque()
    q.append([a,b])

    # if visited[a][b] == False:
    visited[a][b] = True
    while q:
        i,j = q.pop()
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]

            if x < 0 or x >= n or y < 0 or y >=n or visited[x][y]:
                continue

            if color != 'B' and array[x][y] != 'B':
                visited[x][y] = True
                q.append([x,y])
            elif color == 'B' and array[x][y] == 'B':
                visited[x][y] = True
                q.append([x,y])
    return

def bfs(a,b,color):

    q = deque()
    q.append([a, b])
    visited[a][b] = True
    while q:
        i, j = q.pop()

        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]

            if x < 0 or x >= n or y < 0 or y >= n or visited[x][y]:
                continue

            if color == array[x][y]:
                visited[x][y] = True
                q.append([x,y])
    return

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i,j,array[i][j])
            cnt += 1

print(cnt,end=' ')
visited= [[False]*n for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs_blind(i,j,array[i][j])
            cnt += 1
print(cnt)
