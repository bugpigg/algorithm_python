# 알고리즘: 1. n개의 정수를 가지는 배열 A에 대하여 for 문을 돌면서 각 원소의 값을 다음 index의 값과 비교
#          2. 만약 index가 짝수이면서 다음 index의 값보다 작거나 같으면 pass, 아니라면 index 값과 index+1의 값을 스위치
#             만약 index가 홀수이면서 다음 index의 값보다 크거나 같으면 pass, 아니라면 index 값과 index+1의 값을 스위치
# 수행시간: 위 알고리즘은 for 문을 통해 배열 A의 원소들을 하나씩 불러와 비교하므로 O(n)의 수행시간이 소요
def solve(A):
	for idx in range(len(A)):
		if idx == len(A)-1:      # idx가 배열의 마지막 원소를 가리키면 수정된 배열 A 리턴
			return A
		if idx % 2 ==1:          # idx가 홀수이면
			if A[idx] >= A[idx+1]: 
				pass
			else:                  # 조건을 만족시키지 못하면 idx값과 idx+1의 값을 스위치
				temp = A[idx+1]
				A[idx+1] = A[idx]
				A[idx] = temp
		else:                    # idx가 짝수이면
			if A[idx] <= A[idx+1]:
				pass
			else:                  # 조건을 만족시키지 못하면 inx값과 idx+1의 값을 스위치
				temp = A[idx+1]
				A[idx+1] = A[idx]
				A[idx] = temp

def check(B):
	if not (B[0] <= B[1]): return False
	for i in range(1, len(B)-1):
		if i%2 == 1 and not (B[i] >= B[i+1]):
			return False
		if i%2 == 0 and not (B[i] <= B[i+1]):
			return False
	return True		
	
A = [int(x) for x in input().split()]
B = solve(A)
print(check(B))