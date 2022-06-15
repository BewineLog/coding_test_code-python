import sys
T = int(input())

array = [[0],[1],[2,4,8,6],[3,9,7,1],[4,6],[5],[6],[7,9,3,1],[8,4,2,6],[9,1],[0]]

for _ in range(T):
    a,b = map(int,sys.stdin.readline().split())
    a = a % 10
    b = b % len(array[a])

    if a == 1 or a == 5 or a == 6:
        print(a)
    elif a == 0:
        print(10)
    elif b == 0:
        print(array[a][-1])
    else:
        print(array[a][b-1])
