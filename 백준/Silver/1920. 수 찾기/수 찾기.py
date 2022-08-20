import sys

N = int(input())

A = set(map(int, sys.stdin.readline().split()))
M = int(input())
Mlist = list(map(int, sys.stdin.readline().split()))

for i in Mlist :
    print(1 if i in A else 0)
        