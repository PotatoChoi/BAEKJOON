def solution(n, arr1, arr2):
    answer = []
    
    def makearr(arr):
        for i in range(len(arr)):
            table = ''
            num = arr[i]
            while num > 0 :
                num, share = num // 2, num % 2
                table += str(share)
            if len(table) < n:
                table += '0' * (n - len(table))
            arr[i] = table[::-1]
        return arr
    arr1 = makearr(arr1)
    arr2 = makearr(arr2)
    
    for i in range(n) :
        line = ''
        for j in range(n) :
            if arr1[i][j] == '0' and arr2[i][j] == '0' :
                line += ' '
            else :
                line += '#'
        answer.append(line)
            
    return answer