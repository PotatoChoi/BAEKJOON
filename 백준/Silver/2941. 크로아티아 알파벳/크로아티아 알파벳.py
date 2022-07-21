Str = input()
Table = ['c=','c-','dz=','d-','lj','nj','s=','z=']
Count=0
for i in Table:
    if i in Str:
        if i=='dz=':
            Count+=Str.count(i)*2
        else:
            Count+=Str.count(i)*1
        if i=='z=':
            Count-=Str.count('dz=')*1
print(len(Str)-Count)