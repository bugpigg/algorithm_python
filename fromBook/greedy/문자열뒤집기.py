from sys import stdin
s = stdin.readline()
count0 = count1 = 0
f = s[0]
if f == '1':
    count0 += 1
else:
    count1 += 1 

for ch in s[1:]:
    if ch != f:
        if ch == '1':
            count0 += 1
        else:
            count1 += 1
    f = ch
print(min(count0,count1))
