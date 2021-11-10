import sys; input = sys.stdin.readline

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n,m = map(int,input().split())
parent=list(range(n+1))

edges = [list(map(int,input().split())) for _ in range(m)]
edges = sorted(edges,key = lambda x: x[2])


result = last = 0 
for a,b,cost in edges:
    if find(a) != find(b):
        union(a,b)
        result += cost
        last = cost

print(result-last)