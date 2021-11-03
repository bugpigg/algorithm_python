from sys import stdin

n = int(stdin.readline().rstrip())
data = map(int,stdin.readline().rstrip().split())

dp = [0]*(n)
dp[0] = data[0]
dp[1] = max(data[0],data[1])

for i in range(2,n):
    dp[i] = max(dp[i-1],dp[i-2]+data[i])

print(data[-1])