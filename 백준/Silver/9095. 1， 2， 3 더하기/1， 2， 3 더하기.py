n = int(input())

for _ in range(n):
    num = int(input())
    dp = [0] * (num+1)
    
    if num >= 1:
        dp[1] = 1
    if num >= 2:
        dp[2] = 2
    if num >= 3:
        dp[3] = 4
    
    for i in range(4,num+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    print(dp[num])