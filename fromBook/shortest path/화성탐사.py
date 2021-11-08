# input
'''
3
3
5 5 4
3 9 1
3 2 7
5
3 7 2 0 1
2 8 0 9 1
1 2 1 8 1
9 8 9 2 0
3 6 5 1 5
7
9 0 5 1 1 5 3
4 1 2 1 6 5 3
0 7 6 1 6 8 5
1 1 7 8 3 2 3
9 4 0 7 6 4 1
5 8 3 2 4 8 3
7 4 8 4 8 3 4
'''
from sys import stdin
import heapq as hp

INF = int(1e9)
t = int(stdin.readline().rstrip())
ans = []
for _ in range(t):
    n = int(stdin.readline().rstrip())
    field = [list(map(int,stdin.readline().rstrip().split())) for _ in range(n)]
    dx = [0,1]
    dy = [1,0]
    dist = [ [INF]*n for _ in range(n) ]

    def dijkstra(start):
        global n
        h = []
        dist[start[1]][start[2]] = start[0]
        hp.heappush(h,start)
        while h:
            z,x,y = list(hp.heappop(h))
            for i in range(2):
                a,b = x+dx[i],y+dy[i]
                if 0<=a<n and 0<=b<n:
                    if dist[a][b] > field[a][b]+z:
                        dist[a][b] = field[a][b]+z
                        hp.heappush(h,(dist[a][b],a,b))                

    dijkstra((field[0][0],0,0))
    ans.append(dist[n-1][n-1])
print(*ans,sep='\n')