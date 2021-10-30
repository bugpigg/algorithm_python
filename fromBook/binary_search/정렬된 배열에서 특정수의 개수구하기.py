from bisect import bisect_left,bisect_right
from sys import stdin

n,x = map(int,stdin.readline().rstrip().split())
data = list(map(int,stdin.readline().rstrip().split()))

a = bisect_left(data,x)
b = bisect_right(data,x)
if (b-1)== 0:
    print(-1)
else:
    print(b-a)