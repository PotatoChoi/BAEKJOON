import sys

K = int(input())
Nlist = []

for i in range(K) :
    Num = int(sys.stdin.readline())
    if Num != 0 :
        Nlist.append(Num)
    else :
        Nlist.pop()

print(sum(Nlist))