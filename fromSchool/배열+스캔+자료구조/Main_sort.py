def solve(arr):
    majority = len(arr)/2
    arr.sort()
    a = len(arr)//2
    if arr[a]==arr[0] or arr[a]==arr[-1]:
        return arr[len(arr)//2]
    else:
        return -1

cmd = [int(x) for x in input().split()]
print(solve(cmd))