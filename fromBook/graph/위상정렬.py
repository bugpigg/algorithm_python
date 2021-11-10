import sys; input=sys.stdin.readline
from collections import deque

v,e = map(int, input().split())

# 각 노드에 연결된 진입차수는 0으로 초기화
indegree = [0]*(v+1)

# 각 노드에 연결된 간선 정보를 담기 위한 연결 리스트 초기화
graph = [[] for i in range(v+1)]

# 모든 간선 정보 입력 받기
for _ in range(e):
    a,b = map(int,input().split())
    graph[a].append(b)
    indegree[b]+=1

# 위상 정렬 함수
def topology_sort():
    result = []
    q = deque()

    for i in range(1,v+1):
        if indegree[i] == 0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -=1
            if indegree[i] == 0:
                q.append(i)
    
    for i in result:
        print(i,end=' ')

topology_sort()
"""
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4
"""