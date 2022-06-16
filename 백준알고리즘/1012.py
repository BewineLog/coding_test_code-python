import sys
sys.setrecursionlimit(10**9)
T = int(input())

dx = [-1,1,0,0]
dy = [0,0,-1,1]

for _ in range(T):
    M, N, K = map(int,sys.stdin.readline().split())
    array = [[0 for i in range(M)]for j in range(N)]

    # 배추 위치 입력
    for _ in range(K):
        y,x = map(int,input().split())
        array[x][y] = 1

    # grouping
    def group(x,y):
        array[x][y] = 0

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]
            if 0 <= tx <= N-1 and 0 <= ty <= M-1 and array[tx][ty] == 1:
                group(tx,ty)

    cnt = 0
    for i in range(N):
        for j in range(M):
            if array[i][j] == 1:
                cnt += 1
                group(i,j)

    print(cnt)
