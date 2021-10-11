import sys
sys.setrecursionlimit(5000)
def solve(l,s):
	if dp_table[l][s] != None:
		return dp_table[l][s]
	if l == 0:
		if s == 0:
			return 1
		else:
			return 0
	answer = 0
	if L > 1 or S > 1:
		if L==l and S==s:
			start = 1
		else:
			start = 0
		for i in range(start,10):
			if s-i >= 0:
				answer += solve(l-1,s-i)
		dp_table[l][s] = answer
	else:
		answer = 1
	return answer
L, S = [int(x) for x in input().split()]
dp_table = [[None]*(S+1) for _ in range(L+1)] # (L+1)x(S+1) DP table 생성
print(solve(L,S)%2147483647)