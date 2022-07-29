import sys

n = int(input())
array = list(map(int,sys.stdin.readline().rstrip().split()))

dp = [1]*(n+1)

for i in range(n):
    for j in range(i):
        if array[i] > array[j] and dp[j]+1 > dp[i]:
            dp[i] = dp[j]+1

print(max(dp))
