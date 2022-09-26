def solution(s):
    answer = ''
    s = s.split(' ')
    for i in range(len(s)):
        if s[i] != '' :
            if s[i][0].isdigit() :
                answer += s[i][0] + s[i][1:].lower() + ' '
            else :
                answer += s[i][0].upper() + s[i][1:].lower() + ' '
        else :
            answer += s[i] + ' '
    answer = answer[:-1]
    return answer
