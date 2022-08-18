N, K = map(int, input().split())

Nlist = [i for i in range(1, N+1)]

print('<', end='')
while Nlist:
    for i in range(K-1) :
        Nlist.append(Nlist[0])
        Nlist.pop(0)
    print(Nlist.pop(0), end='')
    if Nlist :
        print(', ', end='')
print('>')