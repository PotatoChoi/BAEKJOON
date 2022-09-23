def solution(s):
    answer = True
    try :
        int(s)
    except :
        return False
    if len(s) == 4 or len(s) == 6 :
        answer = True
    else :
        answer = False
    return answer