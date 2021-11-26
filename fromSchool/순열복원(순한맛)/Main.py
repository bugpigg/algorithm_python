def reconstruct(S, L):
	# S, L로부터 A를 재구성해 리턴
	n = len(S)
	a = [0]* n
	for i in range(n):
		a[i] = S[i] + ((n-i-1)-L[i]) + 1	
	return a
# S와 L을 차례로 읽어들임
s = list(map(int,input().split()))
l = list(map(int,input().split()))
print(*reconstruct(s,l))
