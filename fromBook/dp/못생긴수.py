from sys import stdin

n = int(stdin.readline().rstrip())

dp = [0]*n
dp[0] = 1

syn1,syn2,syn3 = 2,3,5
idx1,idx2,idx3 = 0,0,0

for i in range(1,n):
    dp[i] = min(syn1,syn2,syn3)
    if dp[i] == syn1:
        idx1 += 1
        syn1 = dp[idx1] * 2
    if dp[i] == syn2:
        idx2 += 1
        syn2 = dp[idx2] * 3
    if dp[i] == syn3:
        idx3 += 1
        syn3 = dp[idx3] * 5

print(dp[-1])