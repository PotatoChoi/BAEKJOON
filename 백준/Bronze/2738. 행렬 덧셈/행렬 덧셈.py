import sys
N, M = map(int, input().split())
A = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
B = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
C = [print(*[A[j][i]+B[j][i] for i in range(M)]) for j in range(N)]