# DP 점화식: DP 테이블의 DP[j] 같은 경우는 j 번째 단어로 끝나는 문장의 최종 왼쪽 맞춤 penalty 값이다.
#           DP 테이블의 아래와 같이 정의 된다.
#           DP[j] = min( DP[j-1]+(다음 줄에 j 번째 단어만 추가했을때 그 줄의 penalty 값) , 
#                        DP[j-2]+(다음 줄에 j,j-1 번째 단어와 공백 하나를 추가했을때 그 줄의 penalty 값) ,
#                        ...)
#           그리고 다음 줄에 추가된 단어와 공백의 길이가 주어진 페이지 폭 보다 작은 경우만 위 과정에 포함한다.
# 수행시간: 주어진 문장의 단어의 개수를 n이라 할 때, 아래 코드는 두 for문을 통해 최악의 경우 1+2+..+n = n(n+1)/2의 수행시간을 가지므로
#          O(n^2)의 수행시간을 가진다고 말할 수 있다.
import math
W = int(input()) # 페이지 폭 W
words = [0]+[len(string) for string in input().split()] # 단어의 글자수만 저장, 맨 첫번째 원소는 0으로 저장
DP = [0]*len(words) # dp 테이블 정의, (단어 개수 + 1) 만큼의 길이를 가지며 0으로 초기화
for i in range(1,len(words)): # 1번째 원소 부터 탐색
	min_penalty = math.inf # 초기값은 최대값으로 정의
	curr = 0
	# 다음 줄에 현재 단어만 포함하는 경우, 다음 줄에 현재 단어와 바로 이전 한 단어만 포함하는 경우,.. 순으로 모두 탐색하여 최소 penalty 구하기
	for j in range(i,0,-1):
		curr += words[j] # curr에 현재 단어의 길이 더하기
		if i != j: # 만약 curr에 현재 단어만 더해진게 아니라면
			curr += 1 # 공백을 계산하기 위해 1 더하기
		temp = DP[j-1] + (W-curr)**3 # curr 만큼의 줄을 더했을때의 penalty와 이전 DP에 저장된 j-1 번째 원소까지의 최소 penalty 합
		if curr <= W: # 만약 현재 더해진 단어들과 공백의 길이가 페이지 폭보다 작고
			if min_penalty > temp: # 현재 penalty 값이 이전까지 구한 penalty 값보다 작다면
				min_penalty = temp # 최소 penalty 값 갱신
		else: # 페이지 폭을 넘어섰다면
			break # for문 탈출
	DP[i] = min_penalty # DP 테이블에 최소 penalty 값 저장

print(DP[-1]) # 출력값은 DP 테이블의 마지막 원소이다.