import sys; input = sys.stdin.readline
from collections import deque
import copy

v = int(input())
# 진입 차수
indegree = [0]*(v+1)
graph = [[] for _ in range(v+1)]
time = [0]*(v+1)

for i in range(1,v+1):
    data = list(map(int,input().split()))
    time[i] = data[0]
    for d in data[1:-1]:
        indegree[i] +=1
        graph[d].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    # 진입차수 0인것 부터 고려
    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        for i in graph[i]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    
    for i in range(1,v+1):
        print(result[i])

topology_sort()