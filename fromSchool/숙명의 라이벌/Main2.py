from sys import stdin

def solve(kor, jpn, k_goals, j_goals):
	n = len(kor) - 1
	dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

	for i in range(1, n+1):
		for j in range(1, n+1):
			first = dp[i-1][j-1]
			if kor[i]!=jpn[j]:
				if (kor[i]=='W' and k_goals[i] > j_goals[j]) or (jpn[j]=='W' and k_goals[i] < j_goals[j]):
					first +=  k_goals[i] + j_goals[j]
			third = dp[i-1][j]
			fouth = dp[i][j-1]
			dp[i][j] = max(first, third, fouth)
	return dp[n][n]

kor = ' '+stdin.readline().rstrip()
k_goals = [0] + [int(x) for x in stdin.readline().rstrip().split()]
jpn = ' '+stdin.readline().rstrip()
j_goals = [0] + [int(x) for x in stdin.readline().rstrip().split()]
print(solve(kor, jpn, k_goals, j_goals))