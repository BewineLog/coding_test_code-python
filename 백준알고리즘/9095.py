import sys

n = int(sys.stdin.readline())
array = []

for _ in range(n):
    array.append(int(sys.stdin.readline()))

dp = [1,2,4]

for i in range(3,max(array)):
    dp.append(sum(dp[i-3:i]))

for i in array:
    print(dp[i-1])
