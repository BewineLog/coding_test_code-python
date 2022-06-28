import sys
from collections import deque
k = int(sys.stdin.readline())
q = deque()

for _ in range(k):
    n = int(sys.stdin.readline())

    if n != 0:
        q.append(n)
    else:
        q.pop()

s = 0
while q:
    s += q.pop()
print(s)
