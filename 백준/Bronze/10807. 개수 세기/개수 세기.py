import sys

N = int(input())

NList = list(map(int, sys.stdin.readline().rstrip().split()))

v = int(input())

print(NList.count(v))