import sys

n = int(input())
stack = []
result = []
count = 0
No = False

for _ in range(n):
    num = int(sys.stdin.readline().rstrip())
    while count < num:
        count += 1
        stack.append(count)
        result.append('+')
    if stack[-1] == num:
        stack.pop()
        result.append('-')
    else:
        No = True
if No == True:
    print('NO')
else:
    print('\n'.join(result))