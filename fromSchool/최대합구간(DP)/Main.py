# 알고리즘: 1. ToRight[i]는 배열 A[i]를 기준으로 왼쪽 부분의 최대부분합이다.
#          1-1. ToRight[i]는 (A[i-1]+ ToRight[i-1])과 0 중 max 값으로 선정한다.
#          2. ToLeft[j]는 배열 A[j]를 기준으로 오른쪽 부분의 최대부분합이다.
#          2-1. ToLeft[j]는 (A[j+1]+ ToLeft[j+1])과 0 중 max 값으로 선정한다.
#          3, 위와 같이, 배열 A와 길이가 같은 ToRight,ToLeft 배열을 만든다.
#          4. 그리고 배열 A, ToRight, ToLeft를 각 인덱스에 맞추어 더하면 구하고자 하는 결과를 얻는다.
# 수행시간: 배열 A의 길이 만큼 for문을 수행하고, for문 내에서 상수번의 연산을 수행한다. 
#          그리고 최종결과를 출력할때 다시 배열 A의 길이 만큼 for문을 수행하며, for문 내에서 상수번의 연산을 수행한다. 
#          그래서 위의 수행시간을 다 합쳐도 O(n)의 수행시간을 가진다.
def solve(A):
	L = len(A) # 입력받은 배열 A의 길이를 변수 L에 저장
	ToRight = [None]*L # ToRight[i]는 배열 A[i]를 기준으로 왼쪽 부분의 최대부분합이다.
	ToLeft = [None]*L # ToLeft[j]는 배열 A[j]를 기준으로 오른쪽 부분의 최대부분합이다.
	for i in range(L):
		if i == 0: # ToRight의 첫번째 원소, ToLeft의 마지막원소는 0이다.
			ToRight[0] = 0
			ToLeft[L-1] = 0
		else:
			ToRight[i] = max(ToRight[i-1]+A[i-1],0) # ToRight[i]는 (A[i-1]+ ToRight[i-1])과 0 중 max 값으로 선정한다.
			ToLeft[L-i-1] = max(ToLeft[L-i]+A[L-i],0) # ToLeft[j]는 (A[j+1]+ ToLeft[j+1])과 0 중 max 값으로 선정한다.
	return [x+y+z for x,y,z in zip(A,ToRight,ToLeft)] # 배열 A, ToRight, ToLeft를 각 인덱스에 맞추어 더하면 구하고자 하는 결과를 얻는다.


A = [int(x) for x in input().split()]
result = solve(A)
for x in result:
	print(x,end=' ')