import sys

N, M = map(int, input().split())
woods = list(map(int, input().split()))

start = 1
end = max(woods)

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