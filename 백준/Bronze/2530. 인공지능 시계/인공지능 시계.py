A, B, C = map(int, input().split())
D = int(input())
B = B + (C+D)//60
C = (C+D)%60
A = A + B//60
B = B%60
A = A%24
print(A, B, C)