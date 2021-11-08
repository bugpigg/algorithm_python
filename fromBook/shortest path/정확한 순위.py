# 플로이드 워셜로 풀어보자
from sys import stdin

INF = int(1e9)

n,m = map(int,stdin.readline().rstrip().split())
graph = [[INF]*(n+1) for _ in range(n+1)]

# 대각행렬 처리
for i in range(n+1):
    graph[i][i] = 0

# data 입력받기
for _ in range(m):
    a,b = map(int,stdin.readline().rstrip().split())
    graph[a][b] = 1

# 플로이드 워셜 알고리즘
for a in range(1,n+1):
    for b in range(1,n+1):
        for c in range(1,n+1):
            graph[b][c] = min(graph[b][c],graph[b][a]+graph[a][c])

print(graph,sep='\n')

result = 0
for i in range(1,n+1):
    cnt = 0
    for j in range(1,n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            cnt +=1 
    
    if cnt == n:
        result +=1
print(result)