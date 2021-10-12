def solve(A):
    ans = 0
    s = 0
    temp = []
    for a in A:
        b = 1
        while len(temp) != 0:
            if temp[-1][1] >= a:
                b_,a_ = temp.pop()
                s -= a_*b_
                b += b_
            else:
                break
        temp.append([b,a])
        s += a * b
        ans += s
    return ans
A = list(map(int,input().split()))
print(solve(A))