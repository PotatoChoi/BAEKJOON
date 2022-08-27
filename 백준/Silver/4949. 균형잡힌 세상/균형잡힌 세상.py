import sys

while 1:
    Line = sys.stdin.readline().rstrip()
    if Line == '.':
        break
    Val = ''
    for i in Line:
        if (i == '(' or i == '[' or i == ']' or i == ')'):
            Val += i
    for j in range(len(Val)//2):
        Val = Val.replace('()', '').replace('[]', '')
    if Val == '':
        print('yes')
    else:
        print('no')