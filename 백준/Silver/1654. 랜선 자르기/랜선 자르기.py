import sys

K, N = map(int, input().split())
Lines = [int(sys.stdin.readline()) for _ in range(K)]
start, end = 1, max(Lines)

while start <= end:
    mid = (start + end) // 2
    Cut = 0
    for i in Lines:
        Cut += i // mid
    
    if Cut >= N:
        start = mid + 1
    else:
        end = mid - 1

print(end)