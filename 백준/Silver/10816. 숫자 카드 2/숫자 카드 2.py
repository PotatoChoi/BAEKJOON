import sys

N = int(input())

Nlist = map(int, sys.stdin.readline().split())

M = int(input())

Mlist = map(int, sys.stdin.readline().split())

Result = dict()

for i in Nlist:
    if i in Result :
        Result[i] += 1
    else :
        Result[i] = 1

[print(Result[j], end=' ') if j in Result else print(0, end=' ') for j in Mlist]