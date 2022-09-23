def solution(sizes):
    answer = 0
    table = []
    xline = []
    yline = []
    for i in sizes:
        if i[0] >= i[1] :
            table.append([i[0], i[1]])
        else :
            table.append([i[1], i[0]])
    for i in range(len(table)) :
        xline.append(table[i][0])
        yline.append(table[i][1])
    answer = max(xline) * max(yline)
    return answer