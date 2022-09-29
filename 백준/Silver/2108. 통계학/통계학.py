import sys

N = int(input())

Nlist = [int(sys.stdin.readline()) for i in range(N)]

one = sum(Nlist) / N
print(int(one + 0.5) if one >= 0 else int(one - 0.5))

print(sorted(Nlist)[len(Nlist)//2])

Nlist.sort()
cnt = 1
cntNum = dict()
for i in range(1, N) :
    if Nlist[i] == Nlist[i-1] :
        cnt += 1
    else :
        if cnt not in cntNum :
            cntNum[cnt] = []
        cntNum[cnt].append(Nlist[i-1])
        cnt = 1
    if i == N - 1 :
        if cnt not in cntNum :
            cntNum[cnt] = []
        cntNum[cnt].append(Nlist[i])
if len(Nlist) == 1 :
    cntNum[cnt] = Nlist
print(cntNum[max(cntNum)][0] if len(cntNum[max(cntNum)]) == 1 else cntNum[max(cntNum)][1])

print(Nlist[-1] - Nlist[0])