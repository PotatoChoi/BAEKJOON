import sys

N = int(input())

Nlist = []

for i in range(N):
    word = sys.stdin.readline().rstrip()
    if 'push' in word:
        _, num = word.split()
        if 'front' in word:
            Nlist.insert(0, num)
        else:
            Nlist.append(num)
    elif 'pop' in word:
        if len(Nlist) == 0:
            print(-1)
        elif 'front' in word:
            print(Nlist.pop(0))
        else:
            print(Nlist.pop())
    elif 'size' in word:
        print(len(Nlist))
    elif 'empty' in word:
        if len(Nlist):
            print(0)
        else:
            print(1)
    elif 'front' == word:
        if len(Nlist):
            print(Nlist[0])
        else:
            print(-1)
    elif 'back' == word:
        if len(Nlist):
            print(Nlist[-1])
        else:
            print(-1)