A,B = input().split()
A = int(A[-1]+A[-2]+A[-3])
B = int(B[-1]+B[-2]+B[-3])
if A>B:
    print(A)
else :
    print(B)