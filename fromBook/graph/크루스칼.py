from sys import stdin

def find_parent(a):
    if parent[a] != a:
        parent[a] = find_parent(parent[a])
    return parent[a]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    if a>b:
        parent[a] = b
    else:
        parent[b] = a

v,e = map(int,stdin.readline().rstrip().split())
# 부모 테이블 초기화
parent = [0]*(v+1)

edges = []
result = 0

for i in range(1,v+1):
    parent[i] = i

for _ in range(e):
    a,b,cost = map(int,stdin.readline().rstrip().split())
    edges.append((cost,a,b))

edges.sort()

for e in edges:
    cost,a,b = e
    if find_parent(a) != find_parent(b):
        union_parent(a,b)
        result += cost
    print(parent)
print(result)