from sys import stdin

data = [s for s in stdin.readline()[:-1]]

ch = []
num = 0
for d in data:
    if d.isalpha():
        ch.append(d)
    else:
        num += int(d)
ch.sort()
print(ch)
print(''.join(ch) + str(num))
