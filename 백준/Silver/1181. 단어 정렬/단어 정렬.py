import sys
N = int(input())
Table = [sys.stdin.readline().rstrip() for i in range(N)]
Table = set(Table)
Table = list(Table)
Table.sort()
Table.sort(key = len)

print(*Table, sep='\n')