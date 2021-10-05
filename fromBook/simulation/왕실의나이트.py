from sys import stdin

x = stdin.readline()
row = int(x[1])
col = int(ord(x[0])) - int(ord('a')) + 1
data = [row,col]

move = [[2,1],[2,-1],[-2,1],[-2,-1],[1,2],[1,-2],[-1,2],[-1,-2]]

count = 8
for m in move:
    dest = [data[0]+ m[0],data[1]+m[1]]
    s = sum(dest)
    if dest[0] < 1 or dest[0] > 8 or dest[1] < 1 or dest[0] > 8:
        count -= 1
print(count)
