import sys
Inp=sys.stdin.readline
Table = [int(Inp()) for _ in range(int(Inp()))]
for i in sorted(Table):
    sys.stdout.write(f"{i}\n")