import sys

N = int(input())
NList = []

for _ in range(N):
    NList.append(int(sys.stdin.readline().rstrip()))

for i in sorted(NList):
    print(i)