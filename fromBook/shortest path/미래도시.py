# 플로이드 워셜 알고리즘을 이용하여 풀기
from sys import stdin

# 1->k->x 로 가야한다.
n,m = map(int,stdin.readline().rstrip().split())
INF = int(1e9)

dp = [[INF]*(n+1) for _ in range(n+1)]

# 대각 성분 초기화
for i in range(n+1):
    dp[i][i]=0

# 주어진 data에 대하여 dp 초기화
for _ in range(m):
    a,b = map(int,stdin.readline().rstrip().split())
    dp[a][b] = 1
    dp[b][a] = 1
x,k = map(int,stdin.readline().rstrip().split())

for a in range(n+1):
    for b in range(n+1):
        for c in range(n+1):
            dp[b][c] = min(dp[b][c], dp[b][a]+dp[a][c])

ans = dp[1][k]+dp[k][x]
if ans >= int(1e9):
    print(-1)
else:
    print(ans)