import sys

n, length = map(int,sys.stdin.readline().rstrip().split())

lst = []

def backTracking(start):
    if len(lst) == length:
        print(' '.join(map(str,lst)))
        return

    for i in range(start,n+1):
        if i not in lst:
            lst.append(i)
            backTracking(i+1)
            lst.pop()

backTracking(1)
