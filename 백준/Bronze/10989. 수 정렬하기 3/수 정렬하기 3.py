import sys

N = int(input())
Table = [0] * 10000

for i in range(N):
    Table[int(sys.stdin.readline())-1] += 1
    
for i in range(10000):
    if Table[i] != 0:
        for j in range(Table[i]):
            print(i+1)