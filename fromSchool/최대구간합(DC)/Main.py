# 알고리즘: 1. 배열의 크기가 1일때 하나뿐인 원소 리턴 (바닥조건 설정)
#          2. 배열의 반으로 나눠 왼쪽 반 구간에서의 최대구간합 L을 재귀적으로 구함
#          3. 배열의 반으로 나눠 오른쪽 반 구간에서의 최대구간합 R을 재귀적으로 구함
#          4. 만약 배열의 크기가 2라면 양쪽 모두 걸치는 경우의 최대구간합 M은 두 원소의 합으로 설정
#          5. 그렇지 않다면 아래 순서를 따른다.
#             5-1. 배열을 반으로 나눴을 때, 왼쪽 sliced 배열을 대상으로 왼쪽 방향으로 원소들을 더해나갔을 때 최대 합을 ML에 저장
#             5-2. 배열을 반으로 나눴을 때, 오른쪽 sliced 배열을 대상으로 오른쪽 방향으로 원소들을 더해나갔을 때 최대 합을 MR에 저장
#             5-3. 최종 M의 값은 가운데 원소 값과 ML,MR의 합
#          6. 그래서 변수 L,R,M 중 최대값이 최대구간합
# 수행시간: 1. L,R 값을 구할 때 2*T(n/2)의 시간 소요
#          2. M 값을 구할 때 배열을 한번 스캔하므로 n시간이 소요 (배열의 크기=n)
#          그러므로 총 수행시간 T(n) = 2*T(n/2) + cn 이다.
#          n = 2^k이고 T(1) = 1, T(n) = 2^k*T(n/2^k) + kcn = cn + cnlogn이므로 O(nlogn)의 수행시간을 가진다.
def solve(iterable):
	length = len(iterable) # 입력된 배열의 크기를 변수 length로 저장
	if length == 1: # 배열의 크기가 1일때 하나뿐일 배열의 원소 리턴
		return iterable[0]
	P = len(iterable)//2 # 배열의 크기의 반에 해당하는 인덱스
	L = solve(iterable[:P]) # 배열을 반으로 나눴을 때 왼쪽 sliced 배열에서 최대구간합 리턴
	R = solve(iterable[P:]) # 배열을 반으로 나눴을 때 오른쪽 sliced 배열에서 최대구간합 리턴
	if length == 2: # 배열의 크기가 2일때는 양쪽에 걸치는 경우의 최대구간합변수 M은 두 원소의 합으로 지정
		M = sum(iterable) # 이는 L,R,M 중 최대구간합을 선정할 때의 비교를 위함
	else:# 배열의 크기가 3 이상인 경우
		ML,MR,i = 0,0,0
		for idx in range(P-1,-1,-1): # 배열을 반으로 나눴을 때, 왼쪽 sliced 배열을 대상으로 왼쪽 방향으로 원소들을 더해나갔을 때 최대 합을 ML에 저장
			i += iterable[idx]
			if ML < i:
				ML = i
		i = 0
		for idx in range(P+1,length): # 배열을 반으로 나눴을 때, 오른쪽 sliced 배열을 대상으로 오른쪽 방향으로 원소들을 더해나갔을 때 최대 합을 MR에 저장
			i += iterable[idx]
			if MR < i:
				MR = i
		M = ML+MR+iterable[P] # 최종 M의 값은 가운데 원소 값과 왼쪽, 오른쪽 부분에서의 결과의 합
	return max(L,R,M) # L,R,M 중 최대값 리턴

cmd = [int(x) for x in input().split()]
print(solve(cmd))