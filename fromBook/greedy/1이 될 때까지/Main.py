def solve(n,k):
    count = 0
    while True:
        quo = n//k
        remd = n%k
        count += (1+remd)
        if quo == 1:
            break
        else:
            n = quo
    return count 

n,k = map(int,input().split())
print(solve(n,k))