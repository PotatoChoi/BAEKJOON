N = int(input())
Table = [list(input().rstrip()) for i in range(N)]
Width, Height = 0,0
for j in range(N):
    CountW, CountH = 0,0
    for k in range(N):
        if Table[j][k] == ".":
            CountW +=1
        else :
            CountW = 0
        if CountW == 2:
            Width += 1
        if Table[k][j] == ".":
            CountH +=1
        else :
            CountH = 0
        if CountH == 2:
            Height += 1
print(Width, Height)