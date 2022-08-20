import sys

N = int(input())
prt = sys.stdin.readline

A = set(map(int, prt().split()))
M = int(input())
Mlist = list(map(int, prt().split()))

for i in Mlist :
    print(1 if i in A else 0)
        