import heapq as hp
from sys import stdin

INF = int(1e9)
# 노드, 간선
n,m = map(int,stdin.readline().rstrip().split())
start = int(stdin.readline().rstrip())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m+1):
    a,b,c = map(int,stdin.readline().rstrip().split())
    graph[a].append((b,c))

def dijkstra(start):
    h = []
    hp.heappush(h,(0,start))
    distance[start] = 0
    while h:
        dis,now = hp.heappop(h)
        if distance[now] < dis:
            continue
        for i in graph[now]:
            cost = i[1]+dis
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                hp.heappush(h,(cost,i[0]))
                

dijkstra(start)
