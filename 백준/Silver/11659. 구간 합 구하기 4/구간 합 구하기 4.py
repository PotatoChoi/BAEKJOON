import sys
inp = sys.stdin.readline

N, M = map(int, inp().split())

table = list(map(int, inp().split()))
total = [0]
num = 0

for i in table:
    num += i
    total.append(num)

for j in range(M):
    a, b = map(int, inp().split())
    print(total[b] - total[a-1])