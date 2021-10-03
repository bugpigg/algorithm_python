def solve(n,data):
    num_people = 0
    count = 0
    data.sort()
    for p in data:
        num_people += 1
        if num_people >= p:
            count += 1
            num_people = 0
    return count
    
n = int(input())
data = list(map(int, input().split()))
print(solve(n,data))