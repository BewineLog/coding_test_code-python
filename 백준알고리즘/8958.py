import sys

n = int(input())
score = 1
sum = 0

for i in range(n):
    case = list(map(str,sys.stdin.readline()))

    for j in case:
        if j == 'O':
            sum += score
            score += 1
        else:
            score = 1
    print(sum)
    sum = 0
