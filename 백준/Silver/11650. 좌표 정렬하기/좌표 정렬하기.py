import sys

N = int(input())
Table = []

Table = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

[sys.stdout.write(f"{i[0]} {i[1]}\n") for i in sorted(Table)]