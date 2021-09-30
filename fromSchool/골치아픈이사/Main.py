# 알고리즘: 1. n개의 집들 중에서 다른 집까지의 거리의 합이 최소가 되는 집은 (n//2)번째 집
#           2. 그래서 (n//2)번째 집에서 (n-1)개의 다른 집들과의 거리의 합은 아래와 같이 구함
#           if n이 홀수인 경우
#               (n-1)개의 다른 집들과의 거리의 합 = 
#               (n//2)번째 집을 기준으로 왼쪽에 존재하는 집들의 번지수에 -1을 곱해 모두 더한 값 + 오른쪽에 존재하는 집의 번지수들의 합
#           if n이 짝수인 경우
#               홀수의 결과값에 (n//2)번째 집의 번지수를 추가적으로 더해주어야 함
# 수행시간: 위 알고리즘은 for 문을 통해 배열 list의 반을 두 번 호출하므로 O(n)의 수행시간이 소요

def solution(List):
    Idx = len(List)//2
    Sum = 0
    for i in List[:Idx]:
        Sum += i*(-1)
    for i in List[Idx+1:]:
        Sum +=i
    if len(List) % 2 ==1:
        return Sum
    else:
        return Sum + List[Idx]

List = [int(x) for x in input().split()]
List.sort()
print(solution(List))