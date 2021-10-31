import math

W = int(input())
words = [0]+[len(string) for string in input().split()]

DP = [0]*(len(words))

for i in range(1,len(words)):
    min_penalty = math.inf
	curr = 0
    for j in range(i,0,-1):
        curr += words[j]
        if i != j:
            curr += 1
		temp = DP[j-1] + curr**3
        if curr <= W:
            if min_penalty > curr:
                min_penalty = min
        else:
            break
    DP[i] = min_penalty

print(DP[-1])

