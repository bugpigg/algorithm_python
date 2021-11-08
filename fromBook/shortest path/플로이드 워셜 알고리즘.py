from sys import stdin

INF = int(1e9)
# 노드개수
n = int(stdin.readline().rstrip())
# 간선 개수
m = int(stdin.readline().rstrip())
# 2차원 dp 테이블 만들기
dp = [[INF]*(n+1) for _ in range(n+1)]

# 자기자신으로 가는거는 다 0
for i in range(n+1):
    dp[i][i] = 0

# 각 간선 정보 입력받아 초기화
for _ in range(m):
    a,b,c = map(int,stdin.readline().rstrip().split())
    dp[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘
# b 노드에서 c 노드로 가는 길을 a를 거쳐 간다면?
for a in range(n+1):
    for b in range(n+1):
        for c in range(n+1):
            dp[b][c] = min(dp[b][c], dp[b][a]+dp[a][c])

# print result