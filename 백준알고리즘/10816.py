import heapq
import sys

MAX = 10000000 * 2 + 2

n = int(sys.stdin.readline().rstrip())
lst = list(map(int,sys.stdin.readline().rstrip().split()))

m = int(sys.stdin.readline().rstrip())
lst2 = list(map(int,sys.stdin.readline().rstrip().split()))

count = [0] * MAX

while lst:
    count[heapq.heappop(lst)] += 1


for i in range(m):
    print(count[lst2[i]],end = ' ')
