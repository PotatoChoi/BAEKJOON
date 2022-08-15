import sys

N = int(input())
Table = []

for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    Table.append([y,x])

[print(i[1],i[0]) for i in sorted(Table)]