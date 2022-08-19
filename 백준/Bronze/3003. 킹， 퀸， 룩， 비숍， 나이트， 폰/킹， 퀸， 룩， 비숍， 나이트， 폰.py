A = [1, 1, 2, 2, 2, 8]

N = list(map(int, input().split()))

for i in range(len(A)) :
    print(A[i] - N[i], ' ', sep='', end='')