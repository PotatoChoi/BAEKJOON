import sys
N, X = map(int, input().split())
A = list(map(int, sys.stdin.readline().split()))
for i in range(0,len(A)):
    if A[i]<X:
        print(A[i],end=' ')