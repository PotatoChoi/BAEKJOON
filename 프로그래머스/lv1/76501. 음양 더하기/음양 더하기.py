def solution(absolutes, signs):
    answer = 123456789
    numbersum = 0
    for i in range(len(absolutes)) :
        if signs[i] :
            numbersum += absolutes[i]
        else :
            numbersum -= absolutes[i]
    answer = numbersum
    return answer