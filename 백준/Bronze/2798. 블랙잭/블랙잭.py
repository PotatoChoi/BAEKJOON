N, M = map(int, input().split())
Table = list(map(int, input().split()))
Result = []
for i in range(0, len(Table)-2):
    for j in range(i+1, len(Table)-1):
        for k in range(j+1, len(Table)):
            if (Table[i] + Table[j] + Table[k]) <= M :
                Result.append(Table[i] + Table[j] + Table[k])

print(max(Result))