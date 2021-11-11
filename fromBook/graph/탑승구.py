import sys;input=sys.stdin.readline

# 탑승구의 수
g = int(input())
# 비행기의 수
p = int(input())
# 간선 입력받기
edges = []
for i in range(p):
    cost = int(input())
    edges.append(cost)

result = [0] *g
count = 0
for e in edges:
    for i in range(e):
        if result[i] == 0:
            count +=1
            result[i] = 1
            break

print(count)