table = [0]*26
for i in input():
    table[ord(i)-97] += 1
    
print(*table)