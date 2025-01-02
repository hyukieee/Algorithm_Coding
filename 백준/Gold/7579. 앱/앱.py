n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

total_cost = sum(cost)
dp = [0] * (total_cost + 1)

for i in range(n):
    for j in range(total_cost, cost[i] - 1, -1):
        dp[j] = max(dp[j], dp[j - cost[i]] + memory[i])

for i in range(total_cost + 1):
    if dp[i] >= m:
        print(i)
        break