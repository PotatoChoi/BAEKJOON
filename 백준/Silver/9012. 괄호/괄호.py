import sys

T = int(input())

for i in range(T):
    String = sys.stdin.readline().rstrip()
    for j in range((len(String)//2)+2):
        String = String.replace('()', '')
    if String == '':
        print('YES')
    else:
        print('NO')