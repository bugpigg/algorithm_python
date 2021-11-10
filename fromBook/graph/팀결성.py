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

for i in range(m):
    oper,a,b = map(int,input().split())
    if oper == 0:
        union(a,b)
    else:
        if find(a) == find(b):
            print('yes')
        else:
            print('no')
