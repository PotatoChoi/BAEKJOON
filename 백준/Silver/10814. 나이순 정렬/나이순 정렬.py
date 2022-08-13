N = int(input())
Table = {}

for i in range(N):
    Age, Name = map(str, input().split())
    Age = int(Age)
    if Age not in Table :
        Table[Age] = []
    Table[Age].append(Name)
for i in sorted(Table):
    for j in Table[i]:
        print(i, j)