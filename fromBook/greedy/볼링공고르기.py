import math
from sys import stdin

def fact(n,r = 2):
    return math.factorial(n)/(math.factorial(n-r)*math.factorial(2))

n,m = map(int,stdin.readline().split())
data = list(map(int,stdin.readline().split()))

new_dict = {}
for d in data:
    if d in new_dict:
        new_dict[d] += 1
    else:
        new_dict[d] = 1

s = 0
for v in new_dict.values():
    if v > 1:
        s += fact(v)
print(int(fact(n)-s))
