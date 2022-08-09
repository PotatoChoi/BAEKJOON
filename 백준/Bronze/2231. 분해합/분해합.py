N = int(input())
Del = len(str(N))*9
Nori = N-Del
Result = 0
if Nori < 0 :
    Nori = 0
for i in range(Nori, N+1):
    Ncon = i + sum(map(int, str(i)))
    if Ncon == N:
        Result = i
        break

print(Result)