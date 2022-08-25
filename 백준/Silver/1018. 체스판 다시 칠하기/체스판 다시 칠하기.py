import sys

N, M = map(int, input().split())

Table = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(N)]
Clist = []

for i in range(N-7):
    for j in range(M-7):
        Bcount = 0
        Wcount = 0
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if Table[k][l] == 'B':
                        Wcount += 1
                    else:
                        Bcount += 1
                else:
                    if Table[k][l] == 'W':
                        Wcount += 1
                    else:
                        Bcount += 1
        Clist.append(min(Wcount, Bcount))
print(min(Clist))