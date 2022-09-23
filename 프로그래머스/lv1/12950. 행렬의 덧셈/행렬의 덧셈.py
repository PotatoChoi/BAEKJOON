def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)) :
        alist = []
        for j in range(len(arr1[i])) :
            alist.append(arr1[i][j] + arr2[i][j])
        answer.append(alist)
    return answer