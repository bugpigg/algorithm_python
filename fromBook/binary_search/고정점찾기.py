from sys import stdin

def binary_search_fixed_point(array):
    start,end = 0,len(array)-1
    while start <= end:
        mid = (start+end)//2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            end = mid -1
        else:
            start = mid+1
    return -1

n = int(stdin.readline().rstrip())
data = list(map(int,stdin.readline().rstrip().split()))

print(binary_search_fixed_point(data))