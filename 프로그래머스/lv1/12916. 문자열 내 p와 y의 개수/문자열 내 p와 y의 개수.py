def solution(s):
    answer = True
    s = s.upper()
    if (s.count('P') == s.count('Y')) != answer:
        return False
    return True