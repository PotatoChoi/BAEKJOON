Str = input()
Table = [['A','B','C'],['D','E','F'],['G','H','I'],['J','K','L'],['M','N','O'],['P','Q','R','S'],['T','U','V'],['W','X','Y','Z']]
Result=0
for i in Str:
    for j in Table:
        if i in j:
            Result += int(Table.index(j))+3

print(Result)