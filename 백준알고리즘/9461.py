import sys

t = int(sys.stdin.readline())

p = [0,1,1,1] + [0] * 97

for _ in range(t):
    n = int(sys.stdin.readline())
    if n > 3:
        for i in range(3,n+1):
            p[i] = p[i-3] + p[i-2]
    print(p[n])
