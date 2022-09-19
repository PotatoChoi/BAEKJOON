n = input()

alpha = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']

while n != '#' :
    count = 0
    for i in alpha :
        count += n.count(i)
    print(count)
    n = input()