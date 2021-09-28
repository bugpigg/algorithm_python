def solve(arr):
    majority = len(arr)/2
    for a in arr:
        count = 0
        for b in arr:
            if a==b:
                count+=1
        if count > majority:
            return a
    return -1

cmd = [int(x) for x in input().split()]
print(solve(cmd))