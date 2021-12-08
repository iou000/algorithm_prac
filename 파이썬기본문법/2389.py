
N = 18

dp = [-1,-1,1,-1,1,2]

for i in range(6,N):
    if(dp[i-3] == -1 and dp[i-5] == -1):
        dp.append(-1)
    elif(dp[i-3] == -1 or dp[i-5] == -1):
        dp.append(max(dp[i-3],dp[i-5])+1)
    else:
        dp.append(min(dp[i-3],dp[i-5])+1)


print(dp[N-1])