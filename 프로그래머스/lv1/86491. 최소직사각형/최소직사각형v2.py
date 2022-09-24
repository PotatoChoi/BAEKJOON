def solution(sizes):
    answer = 0
    xline = []
    yline = []
    for i in sizes :
        xline.append(max(i))
        yline.append(min(i))
    answer = max(xline) * max(yline)
    return answer
