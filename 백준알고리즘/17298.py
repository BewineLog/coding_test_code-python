import sys
from collections import deque

n = int(input())
array = list(map(int, sys.stdin.readline().rstrip().split()))
stack = deque()
ans = [-1]*n

for i in range(n-1,-1,-1):
    while stack:
        if stack[-1] > array[i]:
            ans[i] = stack[-1]
            stack.append(array[i])
            break
        else:
            stack.pop()

    stack.append(array[i])

print(' '.join(map(str,ans)))
