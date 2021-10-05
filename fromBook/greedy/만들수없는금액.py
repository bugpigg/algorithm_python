from sys import stdin

n = int(stdin.readline())
data = list(map(int,stdin.readline().split()))
data.sort()

f = 1 
for d in data:
    if f < d:
        break
    f += d
print(f)
