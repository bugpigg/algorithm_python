import sys;input=sys.stdin.readline
import math

n = int(input())
p = list(map(int,input().rstrip().split()))
q = list(map(int,input().rstrip().split()))

combine = list(zip(p,q))
combine = sorted(combine,key=lambda x: (x[0],-x[1]))

MAX = 1000000+1
N = 2**(math.ceil(math.log2(MAX))+1)

stree = [0]*N
mtree = [0]*N

def itvsum(start,end,idx,left,right,tree):
    if end < left or start > right:
        return 0
    if left <= start and end <= right:
        return tree[idx]
    mid = (start+end)//2
    return itvsum(start,mid,idx*2,left,right,tree) + itvsum(mid+1,end,(idx*2)+1, left,right,tree)

def update(start,end,idx,value,tree):
    if value < start or end < value:
        return
    tree[idx] += 1
    if start == end:
        return
    mid = (start+end)//2
    update(start,mid,idx*2,value,tree)
    update(mid+1,end,(idx*2)+1,value,tree)

result = [[0,0] for _ in range(n)]
for i in range(n):
    a,b = combine[i][1],combine[n-i-1][1]
    update(0,MAX-1,1,a,stree)
    update(0,MAX-1,1,b,mtree)
    result[i][0] = itvsum(0,MAX-1,1,0,a-1,stree)
    result[n-i-1][1] = itvsum(0,MAX-1,1,b+1,MAX-1,mtree)

ans = 0
for i in range(n):
    a,b = result[i]
    ans += a*b
print(ans)