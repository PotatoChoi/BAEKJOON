import sys

N = int(input())

Nlist = []

for i in range(N):
    word = str(sys.stdin.readline().rstrip())
    if 'push' in word:
        _, push = word.split()
        Nlist.append(push)
    elif 'pop' in word:
        if len(Nlist) == 0:
            print(-1)
        else:
            print(Nlist.pop())
    elif 'size' in word:
        print(len(Nlist))
    elif 'empty' in word:
        if len(Nlist) == 0:
            print(1)
        else:
            print(0)
    elif 'top' in word:
        if len(Nlist) == 0:
            print(-1)
        else:
            print(Nlist[-1])