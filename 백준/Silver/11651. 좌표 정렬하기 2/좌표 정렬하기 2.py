import sys

Inp = sys.stdin.readline

Table = []

for _ in  range(int(Inp())):
    x, y = map(int, Inp().split())
    Table.append([y,x])

[print(i[1],i[0]) for i in sorted(Table)]