import sys
inp = sys.stdin.readline

N = int(inp())

for _ in range(N):
    A, B = map(int, inp().split())
    print(A + B)