import sys; input = sys.stdin.readline

b,n = map(int,input().rstrip().split())
f = [int(input().rstrip()) for _ in range(n)]

dp_square = [ [None]*n for  _ in range(n)]
dp_avg = [ [None]*n for  _ in range(n)]
dp = [ [None]*n for  _ in range(n)]

for i in range(n):
    for j in range(i,n):
        if i ==j:
            dp_square[i][j] = f[j]**2
            dp_avg[i][j] = f[j]
            dp[i][j] = 0
        else:
            dp_square[i][j] = dp_square[i][j-1] + f[j]**2
            dp_avg[i][j] = ((dp_avg[i][j-1]*(j-i)) + f[j]) / (j-i+1)
            dp[i][j] = dp_square[i][j] - (dp_avg[i][j]**2)*(j-i+1)

DP = [[None]*30 for _ in range(n)]
def solve(start,group):
    global n
    group -= 1
    if DP[start][group] != None:
        return DP[start][group]
    if group ==0:
        MIN = dp[start][n-1]
    else:
        MIN = int(1e9)
        for i in range(start,n-group):
            temp = dp[start][i] + solve(i+1,group)
            if MIN > temp:
                MIN = temp
    DP[start][group] = MIN
    return MIN
print(round(solve(0,b),3))