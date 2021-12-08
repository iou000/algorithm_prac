n = 3
data = [4,7,10]

dp=[1, 2, 4]

for i in range(3,max(data)):
    dp.append(dp[i-1] + dp[i-2] + dp[i-3])

for i in data:
    print(dp[i-1])