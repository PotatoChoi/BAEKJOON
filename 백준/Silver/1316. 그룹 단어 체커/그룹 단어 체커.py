def group_checker(N):
    group_cnt = N
    for i in range(N):
        val_group = []
        word = list(map(str, input()))
        j = 0
        for k in word:
            if j == 0:
                val_group.append(k)
            elif word[j-1] != word[j]:
                if k in val_group:
                    group_cnt -= 1
                    break
                else :
                    val_group.append(k)
            j+=1
    return group_cnt

N = int(input())
print(group_checker(N))