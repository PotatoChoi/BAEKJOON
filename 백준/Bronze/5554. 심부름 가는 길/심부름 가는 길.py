time = [int(input()) for _ in range(4)]
print(sum(time) // 60, sum(time) % 60, sep = '\n')