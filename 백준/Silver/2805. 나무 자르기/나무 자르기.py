import sys

N, M = map(int, input().split())
woods = list(map(int, input().split()))
woods.sort()

start = 1
end = woods[-1]

while (start <= end):
    mid = (start + end) // 2
    lumber = 0
    for i in woods:
        if (i > mid):
            lumber += i - mid
    if (lumber >= M):
        start = mid + 1
    else:
        end = mid - 1

print(end)