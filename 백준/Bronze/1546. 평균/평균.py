N=int(input())
Score = list(map(int, input().split()))
total = [Score[i]/max(Score)*100 for i in range(N)]
print(sum(total)/N)