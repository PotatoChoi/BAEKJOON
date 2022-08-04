T = int(input())
for i in range(T):
    Floor = int(input())
    Family = int(input())
    Table = [a for a in range(1, Family+1)]
    for j in range(Floor):
        for k in range(1, Family):
            Table[k] += Table[k-1]
    print(Table[-1])