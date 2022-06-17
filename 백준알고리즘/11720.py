import sys
n = int(input())
lst = list(map(int,input()))
sum = 0

for i in range(n):
    sum += lst[i]
print(sum)
