from sys import stdin

n,m = list(map(int,stdin.readline().split()))
data = [[int(s) for s in stdin.readline()[:-1]] for _ in range(n)]

visited = [[False]*m for _ in range(n)]
dx = [1,0,0,-1]
dy = [0,-1,1,0]

def dfs(x,y):
    global visited,data
    visited[x][y] = True
    for xx,yy in zip(dx,dy):
        X,Y = x+xx,y+yy
        if X>=0 and Y>=0 and X < n and Y < m:
            if data[X][Y] ==0 and visited[X][Y] == False:
                dfs(X,Y)
    return True

cnt = 0
for i in range(n):
    for j in range(m):
        if data[i][j] ==0 and visited[i][j] == False:
            t = dfs(i,j)
            cnt += 1
print(cnt)