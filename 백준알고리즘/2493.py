import sys
from collections import deque

n = int(input())
array = list(map(int, sys.stdin.readline().rstrip().split()))
stack = deque()
ans = [0]*n
for i in range(n):
    while stack:
        if stack[-1][0] >= array[i]:
            ans[i] = stack[-1][1]+1
            stack.append([array[i],i])
            break
        else:
            stack.pop()

    stack.append([array[i],i])
print(' '.join(map(str,ans)))
