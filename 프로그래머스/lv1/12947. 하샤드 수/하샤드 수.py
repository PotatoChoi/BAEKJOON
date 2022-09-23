def solution(x):
    answer = True
    hashade = 0
    for i in str(x) :
        hashade += int(i)
    if x % hashade != 0:
        answer = False
    return answer