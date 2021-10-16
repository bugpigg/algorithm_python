# 알고리즘: 1. n개의 정수가 입력으로 주어질 때 n*2 크기의 2차원 배열 table 을 정의힌다.
#             초기 값으로는 None 값을 저장한다. 
#             table[i][0]의 의미는 i번째 원소로 끝나는 최대구간곱 중 가장 큰 값
#             table[i][1]의 의미는 i번째 원소로 끝나느 최대구간곱 중 가장 작은 값이다
#          2. 주어진 배열 A의 원소들을 하나씩 탐색하며 위 table배열을 채워 나간다.
#          3. table[i][0]는 A[i], table[i-1][0]*A[i], table[i-1][1]*A[i] 수 중 가장 큰 값이다.
#             table[i][1]는 A[i], table[i-1][0]*A[i], table[i-1][1]*A[i] 수 중 가장 작은 값이다.
#          4. 배열 A의 최대 구간곱은 table[:][0]의 원소들 중 가장 큰 값이다.
# 수행시간: 위 알고리즘의 경우 for 문을 통해 배열 A의 원소들을 탐색하는 n 시간과 for 문 내부는 상수시간의 비교연산만 수행하므로
#          총 수행시간 O(n)이다.
def solve(a):
	table = [[None,None] for _ in range(len(a))] # n*2 크기의 2차원 배열 table 을 정의힌다.
	for i,element in enumerate(a): # for 문으로 배열 A의 원소들 탐색
		if i == 0: # 첫번째 원소의 경우
			table[i][0] = a[i]
			table[i][1] = a[i]
		else:
			table[i][1] = min([a[i],table[i-1][0]*a[i],table[i-1][1]*a[i]]) # table[i][1]는 A[i], table[i-1][0]*A[i], table[i-1][1]*A[i] 수 중 가장 작은 값이다.
			table[i][0] = max([a[i],table[i-1][0]*a[i],table[i-1][1]*a[i]])	# table[i][0]는 A[i], table[i-1][0]*A[i], table[i-1][1]*A[i] 수 중 가장 큰 값이다.
	ans = [t[0] for t in table]
	return max(ans) # table[:][0]의 원소들 중 가장 큰 값 반환.
A = list(map(int,input().split()))
print(solve(A)%123464239)