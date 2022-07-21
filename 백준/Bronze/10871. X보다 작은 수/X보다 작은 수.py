N, X = map(int, input().split())
A = list(map(int, input().split()))
[print(A[i],end=' ') for i in range(len(A)) if A[i]<X]