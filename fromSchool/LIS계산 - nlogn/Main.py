# 점화식: DP 테이블의 경우 길이가 index인 증가 부문자열 중 가장 작은 마지막 문자가 저장된다.
#        그렇기에 LIS[i]를 i 번째 문자의 가장 긴 증가 부문자열의 길이라고 한다면
#        i 번째 문자가 DP 테이블에 insert 되는 index에 1을 더한 값이 가장 긴 증가 부문자열의 길이이다.
# 알고리즘: DP 테이블의 DP[i]의 경우는 길이가 i인 증가 부문자열 중 가장 작은 마지막 문자가 저장된다.
#         그렇기에 문자열의 문자를 하나씩 탐색하며 
#         if DP[-1] = DP[i]의 문자보다 현재 문자가 크다면 현재 문자는 
#            가장 긴 증가 부문자열의 개수가 i+1 인 것이므로 DP에 현재문자를 append 하면 된다.
#         else 라면
#             기존 DP 테이블에 현재 문자를 insert 해야한다. 이때 이진 탐색을 통해 inser할 위치를 찾을 수 있다.
#         그렇게 모든 문자에 대하여 탐색을 마치면 DP 테이블의 길이가 주어진 문자열의 가장 긴 증가 부문자열의 길이이다.
# 수행시간: 문자열의 문자를 탐색하는 for 문에서  n 시간이 소요되고, for 문 내부에서 이진탐색을 하여 logn 시간이 소요되므로
#          총 O(nlogn)의 수행시간을 가진다.
def binary_search(array,value): # DP 테이블과 현재 문자를 입력 받아 현재 문자를 insert 할 index 반환
	start = 0
	end = len(array)-1
	while start <= end: # start 포인터가 end 포인터를 역전할때까지
		if array[start] >= value: # 만약 start 포인터가 가리키는 문자가 현재 문자보다 크다면
			return start # start index에 현재 문자를 insert 해야하므로 start 반환
		if array[end] < value: # 만약 end 포인터가 가리키는 문자가 현재 문자보다 작다면
			return end+1 # end+1 index에 현재 문자를 insert 해야하므로 end+1 반환
		mid = (start+end)//2
		if array[mid] == value: # 만약 mid index 문자와 현재 문자가 같다면 mid 반환
			return mid
		elif array[mid] > value: # 만약 mid index 문자와 현재 문자가 같다면 mid 반환
			end = mid-1 # end = mid - 1
		else: # 만약 mid index 문자가 현재 문자보다 작다면
			start = mid+1 # start = mid + 1
	
def LIS_DP(seq):
	DP = [seq[0]] # 빈 DP 테이블 정의
	for ch in seq[1:]: # 문자 하나씩 탐색
		if DP[-1] < ch: # DP의 마지막 원소가 현재문자 보다 작다면 DP에 현재 문자 append
			DP.append(ch)
		else: # DP의 마지막 원소가 현재 문자보다 크다면
			idx = binary_search(DP,ch) # 이진탐색하여 현재문자가 insert 될 index 반환
			DP[idx] = ch # 그 index의 DP 값을 현재 원소로 대체
	return len(DP) # DP 테이블의 길이 리턴

seq = input()  # 알파벳 소문자로만 구성된 string 하나가 입력된다
lis = LIS_DP(seq)
print(lis)