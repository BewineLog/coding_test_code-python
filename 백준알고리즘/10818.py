import sys

n = int(input())
lst = list(map(int,sys.stdin.readline().split()))

if len(lst) != n:
    sys.exit()

print(min(lst),max(lst))

