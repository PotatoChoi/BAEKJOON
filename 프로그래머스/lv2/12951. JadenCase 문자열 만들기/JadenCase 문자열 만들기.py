def solution(s):
    answer = ''
    s = s.split(' ')
    for i in range(len(s)):
        answer += s[i].capitalize() + ' '
    
    answer = answer[:-1]
    return answer