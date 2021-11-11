import sys; input = sys.stdin.readline

def find(a):
    if a != parent[a]:
        parent[a] = find(parent[a])
    return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a> b:
        parent[a] = b
    else:
        parent[b] = a

# 여행지 수 n, 여행 계획 도시의 수 m
n,m = map(int, input().split())
parent = list(range(n+1))

# 여행지 간의 연결 정보 입력받기
for i in range(1,n+1):
    data = list(map(int, input().split()))[i+1:]
    for idx,d in enumerate(data):
        if d == 1:
            union(i,idx+i+1)

# 여행 계획 입력받기
plan = list(map(int, input().split()))
for i in range(len(plan)):
    if i ==0:
        home = find(plan[i])
    else:
        if find(plan[i]) != home:
            print('NO')
            sys.exit()
print('YES')