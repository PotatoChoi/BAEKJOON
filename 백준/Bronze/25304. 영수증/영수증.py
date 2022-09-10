import sys

inp = sys.stdin.readline

X = int(input())
N = int(input())

total = 0

for _ in range(N):
    a, b = map(int, inp().split())
    total += a * b

if total == X :
    print('Yes')
else :
    print('No')