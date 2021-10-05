def solve(s):
    result = 1
    for num in s:
        if num != 0:
            result *= num
    return result

s = [ int(x) for x in input()]
print(solve(s))