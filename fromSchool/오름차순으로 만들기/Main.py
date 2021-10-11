# 알고리즘: 1. nx200 크기의 DP 테이블을 생성한다. n은 입력받는 정수의 개수이다.
#            dp_table[i][j]의 의미는 A[i:]입력이 주어졌다고 가정할 때,
#            i번째 자리의 값을 j값으로 변경할 때 필요한 연산의 최소횟수이다.
#          2. 주어진 n개의 수 중 맨 앞에 있는 수를 x라 할 때, 오름차순를 만족하기 위해 x는 1~x 의 범위를 가질 수 있다.
#          3. 그렇기에 for문을 돌면서 각 x값의 경우에 따라 rtnCount함수를 호출한다.
#          4. rtnCount(idx,prev)는 A[idx:]의 이전 원소가 prev로 확정될 때, 오름차순을 만족시키기 위해 필요한 최소연산횟수를 리턴한다.
#          5. 이때 재귀적으로 최소연산횟수를 계산하며 계산한 값은 DP table에 저장한다.
#             그렇기에 이전에 계산한 연산의 경우 바로 DP table의 값을 리턴한다.
#          6. 바닥조건은 idx가 마지막 원소를 가리킬 때로 한다. 만약 이전 값보다 마지막 원소가 크다면 0을 리턴하고
#             이전값이 크다면 이전값에서 마지막원소의 값을 뺀 값을 리턴한다. 이는 마지막 원소가 오름차순을 만족시키기위해 필요한 최소연산횟수이다.
# 수행시간: 위 알고리즘의 경우 DP table을 이용하여 한번 계산한 값은 저장되어져 재사용된다. 
#         그렇기에 각 자리수를 한번씩 탐방하는데 사용되는 O(n)의 수행시간이 소요된다.
import sys
sys.setrecursionlimit(5000) # recursionlimit을 5000으로 설정하여 최대재귀깊이를 늘려준다.
def rntCount(idx,prev):
	if idx == (len(A)-1): # idx가 마지막 원소를 가리키는 바닥조건인 경우
		if A[idx] >= prev:
			return 0
		else:
			return prev-A[idx]
	if A[idx]>=prev: # 만약 현재 idx의 원소 값이 이전 값보다 크다면, 현재 idx의 값은 (prev~현재원소값)의 범위를 가질 수 있다.
		ans = []
		for cnt,p in enumerate(range(A[idx],prev-1,-1)):
			if dp_table[idx][p] != None: # 만약 이전에 계산한 값으로 DP table에 존재하면 바로 DP table 값 리턴
				cnt = dp_table[idx][p]
			else:
				cnt += rntCount(idx+1,p)
				dp_table[idx][p] = cnt
			ans.append(cnt)
		cnt = min(ans)
	else: # 만약 현재 idx의 원소 값이 이전 값보다 작다면, 현재 idx의 값은 이전 값과 같게 만들어주는 경우 밖에 없다.
		if dp_table[idx][prev] != None: # 만약 이전에 계산한 값으로 DP table에 존재하면 바로 DP table 값 리턴
			cnt = dp_table[idx][prev]
		else:
			cnt = prev - A[idx]
			cnt += rntCount(idx+1,prev)
			dp_table[idx][prev] = cnt
	return cnt

def solve(a):
	ans = []
	for cnt,prev in enumerate(range(a[0],0,-1)):
		cnt += rntCount(1,prev)
		ans.append(cnt)
	return min(ans)

A = [int(x) for x in input().split()]
dp_table = [[None]*200 for _ in range(len(A))] # nx200 DP table 생성
print(solve(A))