n, m = map(int, input().split())
arr = []

for i in range(m):
    days, pages = map(int, input().split())
    arr.append((days, pages))

dp = [0] * (n + 1)

for days, pages in arr:
    for j in range(n, days - 1, -1):
        dp[j] = max(dp[j], dp[j - days] + pages)

print(dp[n])
