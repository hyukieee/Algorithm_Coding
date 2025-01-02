n = int(input())

hp = list(map(int, input().split()))
happy = list(map(int, input().split()))

dp = [0] * 100

for i in range(n):
    loss = hp[i]
    gain = happy[i]
    for j in range(99, loss - 1, -1):
                dp[j] = max(dp[j], dp[j - loss] + gain)


print(max(dp))