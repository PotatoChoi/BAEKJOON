N = int(input())
hansu_cnt = 0
for i in range(1, N+1):
    val_hansu = list(map(int, str(i)))
    if i < 100:
        hansu_cnt += 1
    elif (val_hansu[0] - val_hansu[1]) == (val_hansu[1] - val_hansu[2]):
        hansu_cnt += 1
        
print(hansu_cnt)