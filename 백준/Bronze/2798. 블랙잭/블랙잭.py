N, M = map(int, input().split())
Table = list(map(int, input().split()))
Len = len(Table)
Result = []
for i in range(0, Len-2):
    for j in range(i+1, Len-1):
        for k in range(j+1, Len):
            if (Table[i] + Table[j] + Table[k]) <= M :
                Result.append(Table[i] + Table[j] + Table[k])

print(max(Result))