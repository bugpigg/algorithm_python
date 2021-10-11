# 알고리즘: 1. (L+1)x(S+1) 크기의 DP 테이블을 생성한다.
#            dp_table[i][j]의 의미는 자리수가 i인 수 중에서 각 자리수의 합이 j가 되는 경우의 수이다.
#          2. 주어진 L개의 자리수에 대해서 맨 첫번째자리를 for문을 통해 1~9 수중 하나로 정하고 S와의 차를 비교한다.
#          3. S와의 차를 sub 라 할때, 이 값이 0과 같거나 크다면 재귀적으로 solve(L-1,sub)를 호출하여 
#             L-1자리수의 자연수중 합이 sub일때의 경우의 수를 구하게 한다. 이때는 각 자리에 0~9 수가 가능하다.
#          4. 이런식으로 재귀적으로 함수를 호출하여 자리값의 합을 구하며, 만약 호출한 값이 이미 계산한 값으로 DP table에 존재한다면
#             동일한 계산없이 바로 DP table의 값을 리턴한다.
#          5. 바닥조건은 L=0일 때로 하여 만약 남아있는 S=0이면 조건이 충족된 경우이므로 1을 리턴하고
#             s>0이면 카운트 되지 않게하기 위해 0을 리턴한다.
# 수행시간: 위 알고리즘의 경우 DP table을 이용하여 한번 계산한 값은 저장되어져 재사용된다. 
#         그렇기에 각 자리수를 한번씩 탐방하는데 사용되는 O(L)의 수행시간이 소요된다.
import sys
sys.setrecursionlimit(5000) # recursionlimit을 5000으로 설정하여 최대재귀깊이를 늘려준다.
def solve(l,s):
	if dp_table[l][s] != None: # 만약 이전에 계산한 값으로 DP table에 존재하면 또 계산하지 않고 DP table 값 리턴
		return dp_table[l][s]
	if l == 0: # L=0인 바닥 조건의 경우
		if s == 0: # S=0인 경우 1을 리턴
			return 1
		else: # S>0인 경우는 조건을 만족하지 못한 경우 이므로 카운트 되지 않게 0을 리턴
			return 0
	answer = 0
	if L > 1 or S > 1: # L>1 or S>1인 경우는 재귀적으로 DP table을 채워가며 합을 구함
		if L==l and S==s: # L=l,S=s 인 경우는 첫번째 자리이므로 아래 for문이 1부터 시작
			start = 1
		else: # L!=l,S!=s 인 경우는 두번째이상 자리이므로 아래 for문이 0부터 시작
			start = 0
		for i in range(start,10): # s에서 자리에 올수있는 수를 빼면서 0보다 작거나 크면 재귀적으로 합을 구함
			if s-i >= 0:
				answer += solve(l-1,s-i)
		dp_table[l][s] = answer # 새롭게 구한 값의 경우 DP table에 저장
	else: # L=1,S=1 인경우는 한가지 경우의 수만 존재하므로 답은 1
		answer = 1
	return answer
L, S = [int(x) for x in input().split()]
dp_table = [[None]*(S+1) for _ in range(L+1)] # (L+1)x(S+1) DP table 생성
print(solve(L,S)%2147483647)