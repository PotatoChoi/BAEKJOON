N = int(input())
Result = 0
while N >= 0:
    if N % 5 == 0:
        Result += (N//5)
        print(Result)
        break
    N -= 3
    Result += 1
else :
    print(-1)
    