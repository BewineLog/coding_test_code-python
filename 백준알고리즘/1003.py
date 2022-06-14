n = int(input()) #case

dp = [[0,0] for i in range(41)]
dp[0][0],dp[0][1] = 1,0
dp[1][0],dp[1][1] = 0,1
for i in range(n):
    t = int(input())
    for j in range(2,t+1):
        dp[j][0],dp[j][1] = dp[j-1][0]+dp[j-2][0], dp[j-1][1]+dp[j-2][1]
    print(dp[t][0],dp[t][1])
