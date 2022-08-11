import sys
Inp = sys.stdin.readline
Table = [0] * 10001
for _ in range(int(Inp())):
    Table[int(int(Inp()))] += 1
    
for i in range(1, 10001):
    if Table[i] != 0:
        for _ in range(Table[i]):
            print(i)