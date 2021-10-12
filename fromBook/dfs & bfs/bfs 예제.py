from collections import deque

graph= [[],[2,3],...]
visited = [False] * len(graph)

def bfs(graph,v,visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v,end=' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


bfs(graph,1,visited)