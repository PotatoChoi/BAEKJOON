A,B = input().split()
C=int(input())
A,B = int(A),int(B)
B=B+C
if (B>59):
    A=A+(B//60)
    B=B%60
    if (A>23):
        A=A-24

print(A,B)