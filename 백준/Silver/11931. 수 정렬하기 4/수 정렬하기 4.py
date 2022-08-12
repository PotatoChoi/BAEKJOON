import sys
Inp = sys.stdin.readline
A=[]
for _ in range(int(Inp())):
    A.append(int(Inp()))
A.sort(reverse=True)
print(*A,sep='\n')