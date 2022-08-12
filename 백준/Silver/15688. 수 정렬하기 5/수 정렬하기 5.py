import sys
Inp=sys.stdin.readline
Table = [int(Inp()) for _ in range(int(Inp()))]
print('\n'.join(map(str, sorted(Table))))