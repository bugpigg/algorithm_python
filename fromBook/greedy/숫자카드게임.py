def solve(n,m,data):
    arr = []
    for row in data:
        arr.append(min(row))
    return max(arr)

n,m = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
print(solve(n,m,data))