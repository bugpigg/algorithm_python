from sys import stdin
import heapq as hp

INF = int(1e9)
n,m = map(int,stdin.readline().rstrip().split())
field = [ [] for _ in range(n+1)]
dist = [INF]*(n+1)
for _ in range(m):
    a,b = map(int,stdin.readline().rstrip().split())
    field[a].append(b)
    field[b].append(a)

def dijkstra(start):
    h = [(0,start)]
    dist[start] = 0
    while h:
        dis,idx = hp.heappop(h)
        if dist[idx] < dis:
            continue
        for i in field[idx]:
            cost = dis + 1
            if cost < dist[i]:
                dist[i] = cost
                hp.heappush(h,(cost,i))

dijkstra(1)
a = max(dist[1:])
b = min([ i for i in range(n+1) if dist[i]==a])
c = len([ i for i in range(n+1) if dist[i]==a])
print(b,a,c)