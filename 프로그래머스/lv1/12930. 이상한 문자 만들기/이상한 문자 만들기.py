def solution(s):
    answer = ''
    slist = s.split(' ')
    for i in slist :
        for j in range(len(i)) :
            if j % 2 == 0 :
                answer += i[j].upper()
            else :
                answer += i[j].lower()
        answer += ' '
    answer = answer[:-1]
    return answer