from sys import stdin

n,m = map(int,stdin.readline().rstrip().split())
data = [int(stdin.readline().rstrip()) for _ in range(n)]

dp = [10001]*(m+1)

for i in range(1,m+1):
    if i in data:
        dp[i] = 1
    else:
        for d in data:
            if i-d > 0 and dp[i-d] != 10001:
                dp[i] = min(dp[i-d]+1,dp[i])
print(dp[m])