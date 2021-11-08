# 다익스트라 알고리즘을 사용하여 풀어보자
from sys import stdin
import heapq as hp

n,m,c = map(int,stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    x,y,z = map(int,stdin.readline().rstrip().split())
    graph[x].append((y,z))

INF = int(1e9)
distance = [INF] * (n+1)

def dijkstra(start):
    h = []
    hp.heappush(h,(0,start))
    distance[start] = 0
    while h:
        dis,idx = hp.heappop()
        if distance[idx] < dis:
            continue
        for i in graph[idx]:
            cost = dis + i[1]
            if cost < distance[idx]:
                distance[idx] = cost
                hp.heappush(h,(cost,i[0]))

dijkstra(c)