sci = []
ach = []

for i in range(4) :
    sci.append(int(input()))
    
for j in range(2) :
    ach.append(int(input()))
    
sci.pop(sci.index(min(sci)))
print(sum(sci) + max(ach))