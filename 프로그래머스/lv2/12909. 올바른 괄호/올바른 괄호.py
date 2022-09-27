def solution(s):
    answer = True
    cnt = 0
    for i in s :
        if cnt < 0 :
            break
        if i == '(' :
            cnt += 1
        elif i == ')' :
            cnt -= 1
            
    return cnt == 0