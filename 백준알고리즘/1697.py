import sys
from collections import deque

Max = 10 ** 5

n,k = map(int,sys.stdin.readline().split())

visitedCnt = [0]*(Max+1)

def bfs():
    queue = deque()
    queue.append([n,0])

    while queue:
        idx,cnt = queue.popleft()
        if(idx == k):
            print(cnt)
            break

        pos = [idx-1,idx+1,idx*2]

        for i in pos:
            if 0 <= i <= Max and not visitedCnt[i]:
                visitedCnt[i] = visitedCnt[idx] + 1
                queue.append([i,visitedCnt[i]])
bfs()
