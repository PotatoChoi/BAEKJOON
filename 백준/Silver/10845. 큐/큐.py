import sys

N = int(input())

Nlist = []

for i in range(N):
    word = sys.stdin.readline()
    if 'push' in word:
        _, push = word.split()
        Nlist.append(push)
    elif 'pop' in word:
        if len(Nlist):
            print(Nlist.pop(0))
        else:
            print(-1)
    elif 'size' in word:
        print(len(Nlist))
    elif 'empty' in word:
        if len(Nlist):
            print(0)
        else:
            print(1)
    elif 'front' in word:
        if len(Nlist):
            print(Nlist[0])
        else:
            print(-1)
    elif 'back' in word:
        if len(Nlist):
            print(Nlist[-1])
        else:
            print(-1)