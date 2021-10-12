graph= [[],[2,3],...]
visited = [False] * len(graph)

def dfs(graph,v,visited):
    visitied[v] = True
    print(v,end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph,i,visited)

dfs(graph,1,visited)