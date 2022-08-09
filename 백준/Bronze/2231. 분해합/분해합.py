N = int(input())
Result = 0
for i in range(N+1):
    Ncon = i + sum(map(int, str(i)))
    if Ncon == N:
        Result = i
        break

print(Result)