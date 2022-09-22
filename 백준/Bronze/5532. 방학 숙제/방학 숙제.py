L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

E, F = 0, 0
if (A / C) > (A // C) :
    E += A // C + 1
else :
    E += A // C

if (B / D) > (B // D) :
    F += B // D + 1
else :
    F += B // D

if E >= F :
    print(L - E)
else :
    print(L - F)