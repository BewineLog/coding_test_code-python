import sys

n = int(input())
array = list(map(int,sys.stdin.readline().rstrip().split()))

dp = [1]*(n+1)
af = [1] *(n+1)

for i in range(n):
    for j in range(i):
        if array[i] > array[j] and dp[j] >= dp[i]:
            dp[i] = dp[j] + 1

for i in range(n-1,-1,-1):
    for k in range(n-1,i-1,-1):
        if array[i] > array[k] and af[k] >= af[i]:
            af[i] = af[k] + 1

for i in range(n+1):
    # print(dp[i],af[i])
    dp[i] += af[i]

print(max(dp)-1)
