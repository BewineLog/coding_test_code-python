import sys
input = sys.stdin.readline

n = int(input())

triangle = []

for _ in range(n):
    triangle.append(list(map(int,input().rstrip().split())))
if n == 1:
    print(triangle[0][0])
    sys.exit(0)

for i in range(2):
    triangle[1][i] += triangle[0][0]


for i in range(2,n):
    for j in range(len(triangle[i])):
        triangle[i][j] += triangle[i-1][j] if j == 0 else triangle[i-1][j-1] if j ==(len(triangle[i])-1) else max(triangle[i-1][j-1],triangle[i-1][j])

print(max(triangle[n-1]))
