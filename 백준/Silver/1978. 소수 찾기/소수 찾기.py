import sys

N = int(input())

Table = list(map(int, sys.stdin.readline().split()))

PrimeCount = 0
for i in range(N):
    Count = 0
    for j in range(Table[i]+1):
        if (j > 1) and (Table[i] % j == 0):
            Count += 1
            if (Table[i] == j) and (Count == 1):
                PrimeCount += 1

print(PrimeCount)