N=int(input())
for i in range(N):
    Result=input()
    Score=0
    Count=0
    for i in range(len(Result)):
        if Result[i]=="O":
            Count+=1
            Score+=Count
        else:
            Count=0
    print(Score)