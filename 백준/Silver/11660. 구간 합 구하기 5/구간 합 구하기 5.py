import sys
inp = sys.stdin.readline

N, M = map(int, inp().split())

mset = {0 : [0] * (N + 1)}

for i in range(1, N+1):
    mset[i] = [0] + list(map(int, inp().split()))

for j in range(1, N + 1):
    for k in range(1, N):
        mset[j][k + 1] += mset[j][k]

for k in range(1, N + 1):
    for j in range(1, N):
        mset[j + 1][k] += mset[j][k]
    
for _ in range(M):
    x1, y1, x2, y2 = map(int, inp().split())
    print(mset[x2][y2] - mset[x1 - 1][y2] - mset[x2][y1 - 1] + mset[x1 - 1][y1 - 1])