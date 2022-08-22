import sys

N = int(input())

Slist = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

for i in range(N):
    k = 1
    for j in range(N):
        if (Slist[i][0] < Slist[j][0]) and (Slist[i][1] < Slist[j][1]) :
            k += 1
    print(k, end=' ')