# 점화식: LIS[i]를 i번째 문자로 끝나는 부문자열의 가장 긴 부문자열 길이라고 정의 한다.
#        이때 0 ~ i-1번째의 문자 중 i번째 문자 보다 작은 문자들이 k ~ l 일 때,
#        LIS[i] = max(LIS[k], ... , LIS[l]) + 1로 정의 된다.
# 알고리즘: 1.1차원 DP 테이블을 정의 한다. DP[i]는 i번째 문자로 끝나는 부문자열 중 가장 긴 증가부문자열의 길이이다.
#          2. DP[i]를 채우기 위해서는, 0 ~ i-1 까지의 DP 테이블을 탐색해야 한다.
#          3. 만약 j 번째 문자가 i번째 문자보다 작고, 현재 DP[i]보다 DP[j]+1의 값이 크다면
#             DP[i] = DP[j]+1로 업데이트 한다.
#          4. 1차원 DP 테이블 중 가장 큰 값을 가지는 원소를 리턴하면 된다.
# 수행시간: 수행시간은 n자리를 가지는 문자열 seq에 대하여 바깥 for문은 n번, 안쪽 for문은 평균적으로 (n+1)/2번 이므로
#          두 수를 곱하면 O(n^2)으로 볼 수 있다.
def LIS_DP(seq):
    dp = [1]*len(seq) # DP 테이블 정의
    for i in range(1,len(seq)): # 문자 하나씩 탐색
        for j in range(i): # 이전 문자 하나씩 탐색 
            if seq[i] > seq[j] and dp[i] < dp[j]+1: # 현재 문자보다 작고, dp 값이 더 큰 경우 업데이트
                dp[i] = dp[j]+1
    return max(dp) # DP 테이블에 저장된 값 중 max 값 리턴

seq = input()  # 알파벳 소문자로만 구성된 string 하나가 입력된다
lis = LIS_DP(seq)
print(lis)