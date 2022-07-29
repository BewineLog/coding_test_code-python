import sys

a,b = 1,1

n,m = map(int,sys.stdin.readline().rstrip().split())

for i in range(m):
    a *= (n - i)
    b *= (i + 1)

print(a//b)

