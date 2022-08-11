import sys
from collections import deque

a, b = map(int,sys.stdin.readline().rstrip().split())
deq = deque([(a,1)])
tot = -1

while len(deq) > 0:
    val, cnt = deq.popleft()
    if 2 * val <= b:
        deq.append([2*val,cnt + 1])

    if val*10+1 <= b:
        deq.append([10*val + 1 , cnt+1])

    if 2*val == b or 10*val + 1 == b:
        tot = cnt + 1
print(tot)
