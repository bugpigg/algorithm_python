# 알고리즘: 1. n개의 입력된 정수들을 for문을 돌면서 해시테이블(딕셔너리)에 (key=입력된 정수, value=배열에 등장 횟수) 형식으로 저장한다.
#          2. 그리고 다시 for 문을 돌면서 전체 개수의 절반보다 큰 value 값을 가지는 key를 찾아 리턴한다. 이 key 값이 majority 수이다. 
#          3. 만약 위 조건을 만족시키는 key 값을 찾지 못한다면 majority 수가 없는것이므로 -1을 리턴한다.
# 수행시간: 위 알고리즘은 해시테이블을 사용하여 삽입, 검색 연산에서 O(1)시간이 소요된다. 
#          그러므로 for문에서 n개의 정수를 탐색하는 시간만 카운트하면 되므로 O(n)의 수행시간이 소요된다.
# 수행시간 분석: 1. 해시테이블 사용: O(n)의 수행시간
#               2. 정렬 사용: O(nlogn)의 수행시간 
#                   ㄴ알고리즘: 1. n개의 입력된 정수들 배열
#                              2. majority 수가 존재한다면 (정렬된 배열의 맨뒤의 값과 가운데 있는 값이 같다) or (정렬된 배열의 맨앞의 값과 가운데 있는 값이 같다)
#                                 위 조건이 만족된다면 가운데 있는 값 리턴
#                                 위 조건이 만족되지 않는다면 majority 값이 없는것이므로 -1 리턴
#               3. 이중 for문 사용: O(n^2)의 수행시간
#                   ㄴ알고리즘: 1. 첫 번째 for문에서 count=0
#                              2. 두 번째 for문에서 n개의 입력된 정수들을 탐색하며 첫 번째 for문의 변수 값과 같으면 count 증가
#                              3. 두 번째 for문을 다 돈 후 얻은 count 값을 전체 개수의 절반 값과 비교
#                                 count가 크면 그때의 정수 리턴
#                                 첫 번째 for문까지 다 돌아도 리턴 되지 않았다면 -1 리턴
def solve(arr):
    majority = len(arr)/2
    new_dict = {}
    for a in arr:# 해시테이블에 key,value 값 저장
        if a in new_dict:
            new_dict[a]+=1
        else:
            new_dict[a]=1
    for k,v in new_dict.items():
        if v > majority:# 탐색하며 value값이 전체 개수의 절반 값보다 크다면 그 때의 key 값 리턴
            return k
    return -1

cmd = [int(x) for x in input().split()]
print(solve(cmd))