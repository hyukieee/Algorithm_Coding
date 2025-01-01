
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


n = len(arr)
    
dp = [[0] * (i + 1) for i in range(n)]
    
for j in range(n):
    dp[n-1][j] = arr[n-1][j]
    
for i in range(n-2, -1, -1):
    for j in range(i + 1):
        dp[i][j] = arr[i][j] + max(dp[i+1][j], dp[i+1][j+1])
    

print(dp[0][0])