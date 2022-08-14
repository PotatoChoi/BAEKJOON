import sys

N = int(input())
Table = []

Table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

[print(i[0], i[1]) for i in sorted(Table)]