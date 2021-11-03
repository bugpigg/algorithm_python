from sys import stdin

n = int(stdin.readline().rstrip())

dp = [0]*(n)
dp[0] = 1
dp[1] = 3
for i in range(2,n):
    dp[i] = (dp[i-2]*2 + dp[i-1]) % 796796
print(dp[-1])