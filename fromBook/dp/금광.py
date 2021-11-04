from sys import stdin
from collections import deque

t = int(stdin.readline().rstrip())
data=[]
for _ in range(t):
    n,m = list(map(int,stdin.readline().rstrip().split()))
    d = deque(list(map(int,stdin.readline().rstrip().split())))
    temp_ = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            temp_[i][j] = d.popleft()
    data.append([n,m,temp_])

for idx in range(t):
    n,m,d = data[idx]
    temp = [[0]*m for _ in range(n)]
    for j in range(m):
        for i in range(n):
            if j==0:
                temp[i][j] = d[i][j]
            else: 
                temp_ = [temp[i][j-1]]
                if i-1 >=0:
                    temp_.append(temp[i-1][j-1])
                if i+1 < n:
                    temp_.append(temp[i+1][j-1])
                temp[i][j] = d[i][j] + max(temp_)
    print(temp)
    ans = 0
    for i in range(n):
        if ans < temp[i][m-1]:
            ans = temp[i][m-1]
    print(ans)