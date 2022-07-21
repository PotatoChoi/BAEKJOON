import sys
N=int(input())
Score = list(map(int, sys.stdin.readline().split()))
total = [Score[i]/max(Score)*100 for i in range(N)]
print(sum(total)/N)