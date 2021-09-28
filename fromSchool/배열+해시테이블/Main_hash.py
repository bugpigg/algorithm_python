# 알고리즘: 1. n개의 입력된 정수들을 for문을 돌면서 해시테이블(딕셔너리)에 (key=입력된 정수, value= index) 형식으로 저장한다.
#          2. 그리고 다시 for문을 돌면서 n개의 입력된 정수들에 대해서 target이 되는 정수 k와의 차를 계산한다.
#          3. 이때 이 차와 같은 값을 가지는 해시테이블의 key 값이 존재하면 조건을 만족하는 한 쌍을 찾은것이므로 count를 하나 증가시킨다.
#          4. 그리고 그때의 key값을 가지는 해시테이블의 아이템을 삭제한다.
#          5. 또한 for문을 돌때 num변수가 가리키는 해시테이블의 아이템도 삭제하여야 예외처리가 가능하다.
#          6. 5.번의 step은 다음과 같은 상황을 방지한다. e.g.) k =10, n개의 정수 =[5,2,8] 일때 5.번 step이 없다면 1이 아닌 2가 출력된다.
# 수행시간: 위 알고리즘은 해시테이블을 사용하여 삽입, 삭제 연산에서 O(1)시간이 소요된다. 
#          그러므로 for문에서 n개의 정수를 탐색하는 시간만 카운트하면 되므로 O(n)의 수행시간이 소요된다.
# 수행시간 분석: 1. 해시테이블 사용: O(n)의 수행시간
#               2. 정렬 사용: O(nlogn)의 수행시간 
#               3. k=777, n의 갯수를 10,000 , 100,000 , 1,000,000로 변경해가며 위 두 알고리즘 비교
#                   n의 갯수   10,000  |  100,000   |   1,000,000
#                  해시테이블  0.128sec |  1.52sec   |  17.98sec
#                    정 렬     0.141sec |  1.79sec   |  21.78sec
#               4. n을 키워가며 비교했을 때 해시테이블 방법이 O(n)의 수행시간을 따르고 정렬방법이 O(nlogn)의 수행시간을 따르는것이 입증되어 해시테이블 방법이 더 빠른 수행시간을 보여준다.
def solve(target, arr):
    new_dict ={}
    count = 0
    for idx,num in enumerate(arr):# 해시테이블함수에 key,value 값 저장
        new_dict[num] = idx
    for num in arr:
        if not num in new_dict:# 이 경우는 이전 loop의 num값과 합을 통해 target을 만족해 해시테이블에서 삭제됨
            continue
        else:# num 변수가 가리키는 해시테이블의 아이템을 삭제하여야 예외처리 가능
            del new_dict[num]
        if target-num in new_dict:# target과의 차와 같은 값을 가지는 해시테이블의 key 값이 존재
            count+=1# 카운트 증가
            del new_dict[target-num]# 이후 for문에서의 count 중복 방지를 위해 그때의 key값을 가지는 해시테이블의 아이템삭제
    return count
        
##
# import time
# import random
# start = time.time()
# cmd1 = 777
# cmd2 = random.sample(range(0,10000000),10000000)
##
cmd1 = int(input())
cmd2 = [int(x) for x in input().split()]
print(solve(cmd1,cmd2))
##
# print("time :", time.time() - start)
##