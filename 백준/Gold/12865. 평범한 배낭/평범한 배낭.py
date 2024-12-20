def knapsack(n,k,item):
    dp = [0] * (k+1)
    for weight ,value in item:
        for i in range(k,weight -1, -1):
            dp[i] = max(dp[i], dp[i-weight]+value)
    return dp[k]

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

print(knapsack(N, K, items))