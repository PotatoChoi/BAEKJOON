import sys
Inp=sys.stdin.readline
T=[0]*5**6
for _ in range(int(Inp())):
    T[int(Inp())] += 1
    
for i, j in enumerate(T):
    for _ in range(j):
        sys.stdout.write(f"{i}\n")