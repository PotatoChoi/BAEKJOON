T = int(input())
for i in range(T):
    R,S=input().split()
    R=int(R)
    Result=""
    for j in S:
        Result+=R*j
    print(Result)