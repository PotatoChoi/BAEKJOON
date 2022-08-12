import sys
Inp=sys.stdin.readline
A=[]
for _ in range(int(Inp())):
    A.append(int(Inp()))
for i in sorted(A):
    sys.stdout.write(f"{i}\n")