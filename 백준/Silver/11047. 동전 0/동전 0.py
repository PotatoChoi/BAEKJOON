import sys
inp = sys.stdin.readline

N, K = map(int, inp().split())

klist = [int(inp()) for _ in range(N)]

count = 0

for i in reversed(klist):
    if i <= K:
        count += K//i
        K = K%i

print(count)