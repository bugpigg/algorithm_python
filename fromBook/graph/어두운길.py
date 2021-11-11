import sys; input = sys.stdin.readline

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = parent[a]
    b = parent[b]
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

# 집의 수, 도로의 수 
n,m = map(int,input().split())

# parent
parent = list(range(n))

# sort edges
edges = []
for _ in range(m):
    a,b,cost = map(int,input().split())
    edges.append((cost,a,b))
edges.sort()

ans = 0
for cost,a,b in edges:
    if find(a) != find(b):
        union(a,b)
    else:
        ans += cost

print(ans)