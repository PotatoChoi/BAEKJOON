N=int(input())
if N<10:
    N=N*10
A=N
C=0
while 1:
    B=A%10
    A=A//10+B%10
    A=B*10+A%10
    C+=1
    if A==N:
        print(C)
        break