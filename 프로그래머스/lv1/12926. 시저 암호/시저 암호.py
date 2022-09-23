def solution(s, n):
    answer = ''
    for i in s :
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122 : 
            if i.isupper() :
                i = ord(i) + n
                if i > 90 :
                    i -= 26
                i = chr(i)
            else :
                i = ord(i) + n
                if i > 122 :
                    i -= 26
                i = chr(i)
            answer += i
        else :
            answer += i
    return answer