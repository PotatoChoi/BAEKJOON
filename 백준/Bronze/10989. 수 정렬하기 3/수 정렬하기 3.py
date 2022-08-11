import sys
Inp=sys.stdin.readline
T=[0]*10001
for _ in range(int(Inp())):
    T[int(Inp())] += 1
    
for i, j in enumerate(T):
    k = f"{i}\n"
    for _ in range(j):
        sys.stdout.write(k)