def solve(data,n,m,k):
    data.sort()
    first = data[-1]
    second = data[-2]
    token = (first*k) + second
    quo = m//(k+1)
    rem = m%(k+1)
    return (token*quo) + (first*rem)
# N,M,K에 대한 입력
n,m,k = map(int,input().split())
# N개의 수에 대한 입력
data = [int(x) for x in input().split()]
print(solve(data,n,m,k)) 