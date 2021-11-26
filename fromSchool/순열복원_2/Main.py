# 알고리즘: 1. 주어진 리스트 B의 원소 개수 만큼을 리프노드로 가질 수 있는 segment tree 를 정의한다.
#          2. 리프노드의 초기값을 1로 정의하여 tree를 업데이트한다. 
#             이때 1의 의미는 그 리프노드의 인덱스가 의미하는 B의 원소가 아직 채택되지 않았다는 의미이다.
#          3. B의 가장 마지막 원소 부터 차례대로 탐색하며 tree를 업데이트 한다.
#             마지막 원소 부터 탐색하는 이유는 마지막 원소의 경우 B[-1]+1의 원소 값을 가지는 것을 바로 알 수 있기 때문이다.
#          4. B의 i 번째 원소에 대하여 tree의 업데이트를 수행 한다고 가정 한다.
#             4-1. 루트 노드부터 차례대로 탐색하며 도달한 노드값을 1 감소시킨다.
#             4-2. 왼쪽자식 노드의 값이 B[i]+1의 값과 같거나 크다면 왼쪽 서브트리 탐색,
#                  아니라면 오른쪽 서브트리를 탐색한다
#             4-3. 리프노드에 도달한다면 이는 i번째 원소의 순열값이 도달한 리프노드의 인덱스이다.
#          5. 위와 같은 방식으로 A를 구한다.
#1. 본인이 작성한 알고리즘의 수행시간을 간략히 분석해보자
#   ㄴ 위 알고리즘은 리스트 B의 원소 개수 n만큼 for문을 돌며, 내부에서는 segment tree 탐색에 logn 의 시간이 소요된다.
#2. 수행시간 T(n)을 Big-O료 표기해보자
#   ㄴ for문을 n번 돌며, 내부에서 segment tree 탐색에 logn 의 시간을 소요 하므로 O(nlogn)의 수행시간을 가진다.
# 입력	
import sys; input = sys.stdin.readline
B = list(map(int,input().rstrip().split()))
# segment tree를 0으로 초기화하여 정의
tree = [0]*(len(B)*4)
ans = [0]*len(B)

# 리프노드들을 모두 1로 바꾸며 tree update
def init(start,end,idx):
	# 리프 노드인 경우
	if start == end:
		# 값을 1로 설정
		tree[idx] = 1
	else:
		mid = (start+end)//2
		tree[idx] = init(start,mid,idx*2) + init(mid+1,end,(idx*2)+1)
	return tree[idx]
	
# segment tree update
def update(start,end,idx,value):
	tree[idx] -= 1
	# 리프 노드인 경우
	if start == end:
		# 인덱스 리턴
		return start
	mid = (start+end)//2
	# 왼쪽 서브트리의 남은 빈칸의 개수가 현재값의 조건을 충족한다면
	if tree[idx*2] >= value:
		# 왼쪽 서브트리 값 업데이트
		return update(start,mid,idx*2,value)
	# 오른쪽 서브트리의 남은 빈칸의 개수가 현재값의 조건을 충족한다면
	else:
		# 오른쪽 서브트리 값 업데이트
		return update(mid+1,end,(idx*2)+1,value-tree[idx*2])

# 리프노드의 값을 모두 1로 설정
init(1,len(B),1)
# 주어진 B 리스트의 마지막 원소부터 사용하여 트리 업데이트
for i in range(len(B)-1,-1,-1):
	# update함수가 리턴하는 값은 A[i]
	idx = update(1,len(B),1,B[i]+1)
	ans[i] = idx
# A 출력
print(*ans)