L, P = map(int, input().split())
calP = L*P
num = map(int, input().split())
for i in num :
    print(i - calP, end=' ')