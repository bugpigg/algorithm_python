def solve(target, arr):
    arr.sort()
    frontptr, backptr = 0, len(arr)-1
    count = 0
    while(True):
        if frontptr >= backptr:
            break
        sum_ = arr[frontptr] + arr[backptr]
        if sum_ > target:
            backptr -= 1
        elif sum_ < target:
            frontptr += 1
        else:
            frontptr += 1
            backptr -= 1
            count += 1
    return count
        
##
# import time
# import random
# start = time.time()
# cmd1 = 775
# cmd2 = random.sample(range(0,10000000),10000000)
##

cmd1 = int(input())
cmd2 = [int(x) for x in input().split()]
print(solve(cmd1,cmd2))
##
# print("time :", time.time() - start)
##