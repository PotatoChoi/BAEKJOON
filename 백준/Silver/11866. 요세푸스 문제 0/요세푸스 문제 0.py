N, K = map(int, input().split())

Nlist = [i for i in range(1, N+1)]

i = 0
print('<', end='')
while Nlist:
    i += K-1
    print(Nlist.pop(i%len(Nlist)), end='')
    i = i%(len(Nlist)+1)
    if Nlist:
        print(', ', end='')
print('>')